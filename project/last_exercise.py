import argparse, textwrap
from linearmodels import *
from diagnostic_plot import *
import statsmodels.api as sm
from dataset import Dataset
from linearmodels import *
parser = argparse.ArgumentParser()


parser = argparse.ArgumentParser(prog='testerLogistic',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                                 Logistic regression tester
                                     --------------------------------
                                     This program is used for testing the linear reggersion class 
                                    '''),
        epilog=textwrap.dedent('''\
                                     --------------------------------
                                        for at aditional info view the file
                                     ''')
                    )

# add one argument with defautl value
# and specifying datatype
parser.add_argument("--seed",default=12345, type=int, 
help=textwrap.dedent(" Random state from module thats splits data in to train with default seed value is set to 12345"))


parser.add_argument("--test_split", type=int, default=0.3,help=textwrap.dedent("Percentage split between training and test, default test is set to 30%"))

parser.add_argument("--covariates", nargs="+", type=int, choices=[0, 1, 2, 3],
help=textwrap.dedent("""Specify the wanted indepent varibales in form of a list. 
such as 1 2, this will include column one and two. 0 indicates if you want a constant or not"""))

parser.add_argument("--make_plot", action="store_true",
help=textwrap.dedent(" indicate if you want to make a plot or not, deafult set to true"))


# pass all arguments into an object that retrive
# arguments with property-decorator style
args = parser.parse_args()
print(args)

#Loads the dataset from spector
spector_data = sm.datasets.spector.load()

# Load the covariates and dependent variable into an object of the class DataSet
y = spector_data.endog.values
x = spector_data.exog.values




df = Dataset(x,y)

# Add a constant to the dataset
df.add_constant()

lm1 = LogisticRegression()


# splitting data in too training and test 
x_train, x_test, y_train, y_test = df.train_test(seed = args.seed, test_size=args.test_split)

# slicing covariates
if args.covariates is not None:
    x_train = x_train[:,args.covariates]
    x_test = x_test[:,args.covariates]

lm1.optimize(x_train, y_train, dataIntercept=True)

y_hat = lm1.predict(x_test)

if args.make_plot:
    plot = DiagnosticPlot(lm1)
    plot.plot(y_test,y_hat)

lm1.summary(y_test)
# Model 1: y ~ b0 + b1*x1
"""
model1.linearModel("y ~ b0 + b1*x1")
model1.optimize(x_train,y_train, dataIntercept=True)
y_hat = model1.predict(x_test)
plot1 = DiagnosticPlot(model1)
model1.summary(y_test)
plot1.plot(y_test, y_hat)"""




