import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("D:/VSCode/Python/MachineLearning/tree_data.csv")

# map data
d = {'UK' : 0, 'USA' : 1, 'N': 2}
df['Nationality'] =  df['Nationality'].map(d)

d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# separate features from target
# features = what we are trying to predict *from*
# target = what we are trying *to* predict

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X,y)

tree.plot_tree(dtree, feature_names=features)

plt.show()

# gini refers to quality of split; always [0.0, 0.5]
# 0.0 = all samples have same result
# 0.5 = split is exactly in middle

# samples = # of samples left in branch at this point in decision

# value = [x,y] = of the total samples, x are true, y are false

decision = True if dtree.predict([[40, 10, 7, 1]]) == 1 else False

print("Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?: " + 
      decision)

# Decision trees give different results if run enough times even with same data
# D tree answers are not 100% certain and are based on probability of an outcome