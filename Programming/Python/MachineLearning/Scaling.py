import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

# The standardization method uses this formula:
# z = (x - u) / s
# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.

df = pandas.read_csv("D:\VSCode\Python\MachineLearning\data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:

# When the data set is scaled, you will have to use the scale when you predict values:
df = pandas.read_csv("D:\VSCode\Python\MachineLearning\data.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predicted_CO2 = regr.predict([scaled[0]])
print(predicted_CO2)