from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True)

# K-fold validation
# training data is split into k smaller sets to be used to validate the model
# the model is then trained on k-1 folds of training set where the remaining set
# is used as the validation set 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score

clf = DecisionTreeClassifier(random_state=42)

k_folds = KFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=k_folds)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))


# Stratified K-fold
# accounts for the imbalance in the train and validation sets when classes are imbalanced
# stratify target classes, meaning both sets will have an equal proportion

from sklearn.model_selection import StratifiedKFold

sk_folds = StratifiedKFold(n_splits=5)

scores = cross_val_score(clf, X, y, cv=sk_folds)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))


# There are many more methods for cross validations such as:
# Leave one out where 1 observation is used to validate

# Leave p out where number of p is selected to be used in validation

# Shuffle split where a percentage of data is left out, not to be used in testing or validation



