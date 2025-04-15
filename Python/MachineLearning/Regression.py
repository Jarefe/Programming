import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn.metrics import r2_score


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# linear regression
slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept 

linear_model = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x, linear_model)
plt.show

# polynomial regression
poly_model = np.poly1d(np.polyfit(x,y,3))

poly_line = np.linspace(1,22,100)

plt.scatter(x, y)
plt.plot(poly_line,poly_model(poly_line))
plt.show()

# check for r score

r_score_model = np.poly1d(np.polyfit(x,y,3))

print(r2_score(y,r_score_model(x)))

