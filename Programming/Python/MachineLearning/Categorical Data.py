# machine learning models only accept numeric data, which is why categorical data
# must be converted into numeric values
import pandas as pd
from sklearn import linear_model

cars = pd.read_csv('D:\VSCode\Python\MachineLearning\data.csv')
print(cars.to_string())

# one hot encoding: change categorical data into binary values where 0 = excluded
# and 1 = present

# built in one hot encoding function
ohe_cars = pd.get_dummies(cars[['Car']])
print(ohe_cars.to_string())

# concatenate dummy variables column wise
X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X,y)

# predict the CO2 emission of a VW where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
# ^ VW is the second to last column that was concatenated to original data

print(predictedCO2)

# Dummifying
# the info can be retained using 1 column less than the number of groups 

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
dummies['color'] = colors['color']

print(dummies)