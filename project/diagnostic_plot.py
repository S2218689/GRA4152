from sklearn import metrics
import matplotlib.pyplot as plt
from linearmodels import LinearRegression, LogisticRegression

# A DiagnosticPlot has an object of either linear or logistic regression
class DiagnosticPlot:

    # Initializes a diagnostic plot
    # Checks if the type of object is linear of logistic regression
    def __init__(self, object):
        if isinstance(object, LinearRegression):
            self._type = "linearRegression"
        elif isinstance(object, LogisticRegression):
            self._type = "logisticRegression"
        else:
            raise Exception("Object must be instance of LM")
        self._object = object

    # Plots y against my for a linear regression object
    # Plots the ROC-curve and AUC for a logistic regression object
    def plot(self, y, y_hat):
        if self._type == "linearRegression":
            plt.title("y_test against y_hat")
            plt.xlabel("y_test")
            plt.ylabel("y_hat")
            plt.scatter(y, y_hat)
            plt.show()

        elif self._type == "logisticRegression":
            fpr, tpr, thresholds = metrics.roc_curve(y, y_hat)
            roc_auc = metrics.auc(fpr, tpr)
            display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='ROC curve ')
            display.plot()
            plt.show()






