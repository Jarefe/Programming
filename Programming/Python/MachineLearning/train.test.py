import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x
fig1 = plt.figure("Full dataset")
plt.scatter(x,y)
fig1.show()

# data set illustrates 100 customers in a shop, and their shopping habits
# The x axis represents the number of minutes before making a purchase.
# The y axis represents the amount of money spent on the purchase.

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

fig2 = plt.figure("Training set")
plt.scatter(train_x, train_y)
fig2.show()

fig3 = plt.figure("Testing set")
plt.scatter(test_x, test_y)
fig3.show()

# fit dataset

model = np.poly1d(np.polyfit(train_x, train_y, 4))

line = np.linspace(0,6,100)

fig4 = plt.figure("fitted dataset")
plt.scatter(train_x, train_y)
plt.plot(line, model(line))
fig4.show()

training_r2 = r2_score(train_y, model(train_x))

print("training r2: " + str(training_r2))

testing_r2 = r2_score(test_y, model(test_x))

print("testing r2: " + str(testing_r2))

print("Model prediction at x = 5: " + str(model(5)))


input() # keeps figures alive