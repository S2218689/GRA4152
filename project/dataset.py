import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
from csv import reader

# This module defines the Dataset class and its subclass CsvDataset
# A dataset has x and y-values, are row or column oriented, and can be scaled
class Dataset:
    # Initialize the dataset
    # @param x are the independent variables
    # @param y is the dependent variable
    # @param roworiented is the how the data is stored
    # @param scaled determines if the dataset should be scaled or not
    def __init__(self, x, y, rowOriented=True, scaled=False):
        self._x = x
        self._y = y
        self._hasIntercept = False #Whether data has an intercept added to it
        self._x_te = None #test data for the x-variables
        self._x_tr = None #training data for the x-variables
        self._y_te = None #test data for the y-variable
        self._y_tr = None #train data for the y-variable

        # Checks if y and x are numpy arrays
        # If not raises a type error
        if not isinstance(y,np.ndarray):
            raise TypeError("y must be a numpy array")
        elif not isinstance(x,np.ndarray):
            raise TypeError("x must be a numpy array")

        # Scales the dataset if scaled is True
        if scaled:
            self._x = MinMaxScaler().fit_transform(x)
        # Transposes the x-data if it is column oriented
        if rowOriented != True:
            self._x = self.transpose(self._x)
     

    # Adds ones to the left side of each row of the x-data
    # Sets hasIntersept to True since the constant has been added
    def add_constant(self):
        len_samples = self._x.shape[0]
        ones = np.repeat(1, len_samples).reshape(len_samples,1)
        self._x = np.concatenate((ones,self._x),axis=1)
        self._hasIntercept = True

    # Divides the data into x and y train and test datasets based on an random index
    # @param test_size is the share of data used for testing.
    # @param seed is the seed value the random number generator starts with
    # @return the x_train, y_train, x_test and y_test as numpy arrays
    def train_test(self, test_size=0.3, seed=None):
        if seed:
            random.seed(seed)
        n = round(len(self._x) * test_size)  # The number of rows in the test sample
        tr_i = random.sample(range(len(self._x)), n)  # Gets a random sample of indexes

        self._x_te = self._x[tr_i]
        self._x_tr = np.delete(self._x, tr_i, axis=0)
        self._y_te = self._y[tr_i]
        self._y_tr = np.delete(self._y, tr_i, axis=0)

        return self._x_tr, self._x_te, self._y_tr, self._y_te

    # @return the x-data
    @property
    def x(self):
        return self._x

    # @return the training x-data
    @property
    def x_tr(self):
        return self._x_tr

    # @return the testing x-data
    @property
    def x_te(self):
        return self._x_te

    # @return the y-data
    @property
    def y(self):
        return self._y

    # @return the training y-data
    @property
    def y_tr(self):
        return self._x_tr

    # @return the testing y-data
    @property
    def t_te(self):
        return self._x_te

    # Transposes the data
    # Assumes data is a numpy object
    def transpose(self, data):
        return np.transpose(data)


# A csv dataset generated numpy arrays based on a csv file
class CsvDataSet(Dataset):
    def __init__(self, file, rowOriented = True, scaled = False):
        data = []
        with open(file, "r", newline="") as file:
            csvReader = reader(file)
            for row in csvReader:
                data.append(row)

        data = np.array(data, dtype=np.float32)

        # If CSV-data is column oriented it gets transposed
        if not rowOriented:
            data = self.transpose(data)
        x = data[:,1:]
        y = data[:,0]
        # Calls the super class constructor
        super().__init__(x,y, scaled = scaled)















