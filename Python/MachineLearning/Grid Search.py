# one method to determine best value for C (the parameter that controls regularization
# which affects the model complexity) is to try out different values and pick
# the value that gives the best score; this is a technique known as grid search

# if selecting values for multiple parameters, all combinations will be evaluated

# higher values of C tell the model the training data resembles real world info
# which will place a greater weight on the training data

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

X = iris['data']
y = iris['target']

# default value for C in log regr is 1

logit = LogisticRegression(max_iter=10000)

print(logit.fit(X,y))

print(logit.score(X,y))

C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

scores = []

for choice in C:
    logit.set_params(C=choice)
    logit.fit(X,y)
    scores.append(logit.score(X,y))

# scores closer to 1 means higher accuracy
print(scores)

# if model corresponds too closely to data, it may not be great at predicting unseen
# data, which is referred to as overfitting. this is why it is best to separate
# datasets into training and testing sets 
