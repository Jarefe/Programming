# aims to solve classification problems by predicting categorical instead of
# continuous outcomes
import numpy as np
from sklearn import linear_model

def logit2prob(logr,x):
    log_odds  = logr.coef_ * x + logr.intercept_
    odds = np.exp(log_odds)
    probability = odds / (1 + odds)
    return probability

# X represents the size of a tumor in centimeters
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)

# Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
# y represents whether or not the tumor is cancerous (0 for "No", 1 for "Yes").
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(np.array([3.46]).reshape(-1,1))
print(predicted)


log_odds = logr.coef_
odds = np.exp(log_odds)

# an increase in 1mm increases the odds of it being cancerous by odds%
print(odds)

# probablity that each tumor is cancerous
print(logit2prob(logr, X))