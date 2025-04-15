# AUC = area under the receiver operating characteristic (ROC) curve
# The ROC plots the true positive rate vs the false positive rate at different
# classification thresholds, where the different thresholds are 
# different probability cutoffs that separate the two classes into binary classification

# Imbalanced data
# in cases where a majority of the data is one value, we can obtain high 
# accuracy for the model by predicting the majority class

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

n = 10000
ratio = .95
n_0 = int((1-ratio) * n)
n_1 = int(ratio * n)

y = np.array([0] * n_0 + [1] * n[1])

import matplotlib.pyplot as plt

def plot_roc_curve(true_y, y_prob):
    """
    plots the roc curve based on the probabilities
    """

    fpr, tpr, thresholds = roc_curve(true_y, y_prob)
    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

# higher AUC score is better even if 2 models have the same accuracy