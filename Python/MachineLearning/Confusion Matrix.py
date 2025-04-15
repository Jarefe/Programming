# a confusion matrix is used in classification problems to asses where errors
# in the model are made

# Rows = actual classes the outcomes should have been
# Columns = predictions made
# Allows us to see which predictions are wrong

# Confusion matrices can be created by predictions made from logistic regression

import numpy
from sklearn import metrics
import matplotlib.pyplot as plt

actual = numpy.random.binomial(1, .9, size = 1000)
predicted = numpy.random.binomial(1, 0.9, size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels= [0,1])
cm_display.plot()
plt.show()

# top left = true negative
# top right = false positive
# bottom left = false negative
# bottom right = true positive

# true = accurate prediction
# false = incorrect prediction

accuracy = metrics.accuracy_score(actual, predicted)

precision = metrics.precision_score(actual, predicted)

# sensitivity = how good model is at predicting positives
sensitivity_recall = metrics.recall_score(actual, predicted)

# specificity = how well model predicts negative results
specificity = metrics.recall_score(actual, predicted, pos_label=0)

# f score = "harmonic mean" of precision and sensitivity
# considers both false postives and negatives and is good for imbalanced datasets
# does not take into consideration true negatives
f1_score = metrics.f1_score(actual, predicted)

print({"Accuracy":accuracy,"Precision":precision,"Sensitivity_recall":sensitivity_recall,"Specificity":specificity,"F1_score":f1_score})