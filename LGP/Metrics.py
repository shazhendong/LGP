# This file implements metrics including classification metrics and regression (to come)
# Reference: https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics

from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss

def accuracy(actual, pred, balanced=False):
    if balanced == False:
        return accuracy_score(actual, pred)
    else:
        return balanced_accuracy_score(actual, pred)

def recall(actual, pred, ave='weighted'):
    return recall_score(actual, pred, average=ave)

def precision(actual, pred, ave='weighted'):
    return precision_score(actual, pred, average=ave)

def f1Score(actual, pred, ave='weighted'):
    return f1_score(actual, pred, average=ave)

def logLoss(allLabels, pred):
    return log_loss(allLabels, pred)