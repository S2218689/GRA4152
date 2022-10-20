from scipy.optimize import minimize
from sklearn.metrics import roc_auc_score
import numpy as np

np.set_printoptions(suppress=True)


# This module defines the abstract class LM.
# It represents the structure for how to implement a Linear regression model
class LM:

    # Constructor which defines all the instance variables
    def __init__(self):
        self._beta = None  # the β parameters
        self._intercept = None  # defines the intercept of the model
        self._model_rep = None  # string representation of the model
        self._dataIntercept = None  # variable that holds information about the data
        self._y_hat = None  # variable that holds the predicted dependant variables from the model
        self._covariates = []  # list with the covariates

    # Method that takes in a string that specifies the independent and dependent variables we want the model to use
    # sets self._model_rep to the string
    # @model_rep is the string that represents the model
    def linearModel(self, model_rep):
        self._model_rep = model_rep.lower()
        # Loops over all the dependent variables and adds them to self._covariates
        for cov in self._model_rep.split("~")[1].split("+"):
            cov = cov.strip()
            # If b0 is in the self._model_rep we include intercept in the data
            if cov == "b0":
                self._intercept = True
                self._covariates.append(0)
            else:
                cov = cov.split("*")[-1]
                self._covariates.append(int(cov[-1]))

    # Abstract class
    def fit(self, params, x, y):
        raise NotImplementedError

    # Abstract class
    def predict(self, x):
        raise NotImplementedError

    # Abstract class
    def diagnosis(self, y):
        raise NotImplementedError

    # @return the self._beta and the intercept if its exists
    @property
    def params(self):
        if self._intercept is not None:
            return [self._intercept] + list(self._beta)
        else:
            return self._beta

    # Uses scipy minimize function to find the optimum parameters for our betas and intercept
    # @ is a numpy-array of the independent variables
    # @y is a numpy-array of the dependent variable
    # @dataIntercept tells the program if the user has added a column with 1 in the dependent variable
    # @init_value sets the initial value of the parameters that are going to be optimised in the scipy minimize function
    def optimize(self, x, y, dataIntercept=False, init_val=1):
        # sets instance variable of dataIntercept
        self._dataIntercept = dataIntercept
        if self._model_rep:
            if not self._dataIntercept:
                # If there is no column with 1 for intercept in data we can set the correct index for covariates
                self._covariates = [x - 1 for x in self._covariates]
            # Sets x to the correct data based on model representation
            x = x[:, self._covariates]
        else:
            # If there are no model representation we set the covariates to all the columns in the data
            self._covariates = list(range(x.shape[-1]))
        len_samples, len_params = x.shape
        init_params = np.repeat(init_val, len_params)
        # Uses minimize to find the optimum parameters for model
        results = minimize(self.fit, init_params, args=(x, y))

        # Sets self._intercept and self._beta to optimized parameters
        if self._dataIntercept and (self._intercept or not self._model_rep):
            self._intercept = results["x"][0]
            self._beta = results['x'][1:]
        else:
            # Sets self._beta beta if there are no intercept
            self._beta = results["x"][0:]

    # @return the self._model_rep
    @property
    def model(self):
        return self._model_rep

    # __repr__ method which is called on if the object is printed
    # @return the string representation of the dependent and independent variables
    def __repr__(self):
        # If no model representation is set it returns "I am a LinearModel
        if self._model_rep is None:
            return "I am a LinearModel"

        # If self._beta is None we return the specified model but with 0 in all the betas and the intercept
        elif self._beta is None:
            res = ""
            last = ""
            for letter in self._model_rep:
                if last == "b":
                    last = ""
                    continue
                if letter == "b":
                    res += "0"
                else:
                    res += letter
                last = letter
            return res

        # If self._intercept is not None we return the model representation with the betas inplace of the letter b
        # and self._intercept
        elif self._intercept is not None:
            res = f"y ~ {round(self.params[0], 2)}"
            for i, param in enumerate(self.params[1:]):
                res += " + "
                res += f"{round(param, 2)}*x{i + 1}"
            return res

        # If self._intercept is in model we return the model representation with the betas inplace of the letter b
        else:
            res = f"y ~ "
            for i, param in enumerate(self.params):
                res += f"{round(param, 2)}*x{i} "
            return res

    # summary method prints the Model summary with information about the model representation, fitted parameters and
    # the scoring of the model.
    # @y_test is the unseen independent variable that we score the model based on.
    def summary(self, y_test):
        # uses self.__class__.modelName to access the class variable for printing type of model.
        print(f"------------------------- Model summary {self.__class__._modelName} ------------------------- ")
        print("Model:", self)
        print("Fitted parameters:", self.params)
        print("Model accuracy:", self.diagnosis(y_test))
        print("-----------------------------------------------------------------------------------")


# This module defines the LinearRegression class
# which inherits from the LM class

# A linear regression with its own fit, predict and diagnosis methods
class LinearRegression(LM):
    _modelName = "Linear Regression"

    # Constructor which initiates the object
    def __init__(self):
        # Calls the super class constructor
        super().__init__()

    # Calculates the deviance of the model
    # @return the total model deviance
    # @params is parameters used in minimisation
    # @x is a numpy-array of the independent variables
    # @y is a numpy-array of the dependent variable
    def fit(self, params, x, y):
        y_pred = np.dot(x, params)
        dev = (y - y_pred) ** 2

        return np.sum(dev)

    # Estimates and returns y based on the independent variables
    # @x is a numpy-array of the independent variables
    # @return y_hat
    def predict(self, x):
        # Checks if self._intercept is not None
        if self._intercept is not None:
            x = x[:, self._covariates[1:]]
            # If model has intercept add self._intercept
            self._y_hat = np.dot(x, self._beta) + self._intercept
        else:
            # if self._intercept is None
            x = x[:, self._covariates]
            # Intercept does not exist in this model
            self._y_hat = np.dot(x, self._beta)
        return self._y_hat

    # Calculates R-squared for the model
    # @y is a numpy array of the dependent variable
    # @return R-squared
    def diagnosis(self, y):
        SST = ((y - y.mean()) ** 2).sum()
        # y_hat is the predicted y values
        SSE = ((y - self._y_hat) ** 2).sum()
        r2 = 1 - SSE / SST
        # Rounds the r2 to 4 decimals
        return round(r2, 4)


# This module defines the LogisticRegression class
# which inherits from the LM class

# A logistic regression with its own fit, predict and diagnosis methods
class LogisticRegression(LM):
    _modelName = "Logistic Regression"

    # Initialize the LogisticRegression
    def __init__(self):
        super().__init__()

    # Calculates the deviance of the model
    # @return the total model deviance
    # @params is parameters used in minimisation
    # @x is numpy-arrays of the independent variables
    # @y is numpy arrays of the dependent variable
    def fit(self, params, x, y):
        y_pred = np.dot(x, params)
        dev = np.log(1 + np.exp(y_pred)) - y * y_pred
        return np.sum(dev)

    # Estimates y based on independent variables
    # @x is numpy-arrays of the independent variables
    # @return y_hat
    def predict(self, x):
        if self._intercept is not None:
            x = x[:, self._covariates[1:]]
            lin = np.dot(x, self._beta) + self._intercept
        else:
            x = x[:, self._covariates]
            lin = np.dot(x, self._beta)
        self._y_hat = np.exp(lin) / (1 + np.exp(lin))
        return self._y_hat

    # Calculates the area under the ROC curve
    # @y is numpy arrays of the dependent variable
    # @return the auc (area under curve)
    def diagnosis(self, y):
        # y_hat is the predicted y values
        auc = roc_auc_score(y, self._y_hat)
        # rounds the decimals to 4
        return round(auc, 4)
