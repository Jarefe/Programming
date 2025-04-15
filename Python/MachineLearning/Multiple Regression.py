import pandas
from sklearn import linear_model

dataframe = pandas.read_csv("D:\VSCode\Python\MachineLearning\data.csv")

X = dataframe[['Weight', 'Volume']] # Independent variables capitalized
y = dataframe['CO2'] # dependent variables lowercase

regr = linear_model.LinearRegression()
regr.fit(X,y)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predicted_CO2 = regr.predict([[2300, 1300]])
print("Predicted CO2: " + str(predicted_CO2))
print("Regression coefficients [Weight, Volume]: " + str(regr.coef_))