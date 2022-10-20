from linearmodels import LinearRegression
from diagnostic_plot import DiagnosticPlot
from dataset import CsvDataSet
import statsmodels.api as sm

# Loads the dataset read_estate.csv into an object of type CsvDataSet
df = CsvDataSet("real_estate.csv", scaled=True)

# Add constant to dataset
df.add_constant()

# Model 1: y ~ b0 + b1*x2 + b2*x3 + b2*x3+ b3*x4
linreg1 = LinearRegression()
linreg1.linearModel("y ~ b0 + b1*x2 + b2*x3 + b3*x4")
linreg1.optimize(df.x, df.y, dataIntercept=True)
y_hat = linreg1.predict(df.x)
linreg1.summary(df.y)
plot1 = DiagnosticPlot(linreg1)
plot1.plot(df.y, y_hat)

# Model 2: y ~ b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5
linreg2 = LinearRegression()
linreg2.linearModel("y ~ b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5")
linreg2.optimize(df.x, df.y, dataIntercept=True)
y_hat = linreg2.predict(df.x)
linreg2.summary(df.y)
plot2 = DiagnosticPlot(linreg2)
plot2.plot(df.y, y_hat)

# Model 3: y ~ b1*x1
linreg3 = LinearRegression()
linreg3.linearModel("y ~ b1*x1")
linreg3.optimize(df.x, df.y, dataIntercept=True)
y_hat = linreg3.predict(df.x)
linreg3.summary(df.y)
plot3 = DiagnosticPlot(linreg3)
plot3.plot(df.y, y_hat)


