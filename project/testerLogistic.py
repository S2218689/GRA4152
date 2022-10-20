

from linearmodels import LogisticRegression
from diagnostic_plot import DiagnosticPlot
import statsmodels.api as sm
from dataset import Dataset




#Loads the dataset from spector
spector_data = sm.datasets.spector.load()

# Load the covariates and dependent variable into an object of the class DataSet
y = spector_data.endog.values
x = spector_data.exog.values
df = Dataset(x,y)

# Add a constant to the dataset
df.add_constant()


# Create a train and test data set using the seed value 12345.
# The test data set to default of 30% of the data.
x_train, x_test, y_train, y_test = df.train_test(seed = 12345)

#Define and fit model parameters some models with the train data set
model1 = LogisticRegression()

# Model 1: y ~ b0 + b1*x1
model1.linearModel("y ~ b0 + b1*x1")
model1.optimize(x_train,y_train, dataIntercept=True)
y_hat = model1.predict(x_test)
plot1 = DiagnosticPlot(model1)
model1.summary(y_test)
plot1.plot(y_test, y_hat)

# Model 2: y ~ b0 + b1*x1 + b2*x2
model2 = LogisticRegression()
model2.linearModel("y ~ b0 + b1*x1 + b2*x2")
model2.optimize(x_train,y_train, dataIntercept=True)
y_hat = model2.predict(x_test)
plot2 = DiagnosticPlot(model2)
model2.summary(y_test)
plot2.plot(y_test, y_hat)



# Model 3: y ~ b0 + b1*x1 + b2*x2 + b3*x3
model3 = LogisticRegression()
model3.linearModel("y ~ b0 + b1*x1 + b2*x2 + b3*x3")
model3.optimize(x_train,y_train, dataIntercept=True)
y_hat = model3.predict(x_test)
plot3 = DiagnosticPlot(model3)
model3.summary(y_test)
plot3.plot(y_test, y_hat)



