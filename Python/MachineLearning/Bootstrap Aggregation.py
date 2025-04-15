# aka Bagging: attempts to resolve overfitting by improving accurace and performance
# of algorithms.

# it takes random subsets of an original dataset, with replacement, and fits either
# a classifier or regressor to each subset

# the predictions for each subset are then aggregated through majority vote
# for classification or averaging for regression

# this is a continuation of the concept of decision trees


# test out base classifier first that way there is a baseline value to compare to
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

data = datasets.load_wine(as_frame=True) # as frame saves the feature names when loading

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.25,random_state=22)

dtree = DecisionTreeClassifier(random_state=22)
dtree.fit(X_train,y_train)

y_pred = dtree.predict(X_test)

print("Train data accurace:",accuracy_score(y_true=y_train,y_pred=dtree.predict(X_train)))
print("Test data accuracy:",accuracy_score(y_true=y_test, y_pred=y_pred))


# creating and using bagging classifier

from sklearn.ensemble import BaggingClassifier

estimator_range = [2,4,6,8,10,12,14,16]

# default parameter for base classifier in BaggingClassifier is DecisionTreeClassifier,
# so no need to set it when instantiating Bagging model

models = []
scores = []

for n_estimators in estimator_range:

    # Create bagging classifier
    clf = BaggingClassifier(n_estimators= n_estimators, random_state= 22)

    # Fit the model
    clf.fit(X_train, y_train)

    # Append model and scores to lists
    models.append(clf)
    scores.append(accuracy_score(y_true=y_test, y_pred=clf.predict(X_test)))

# Visualize improvement in model performance

import matplotlib.pyplot as plt

# Generate plot of scores against number of estimators
plt.figure(figsize=(9,6))
plt.plot(estimator_range, scores)

# Adjust labels and font
plt.xlabel("n_estimators", fontsize = 18)
plt.ylabel("score", fontsize = 18)
plt.tick_params(labelsize = 16)

plt.show()