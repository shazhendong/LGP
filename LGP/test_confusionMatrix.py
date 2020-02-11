import Evaluation
import numpy as np


y_true = [0, 1, 0, 1]
y_pred = [1, 1, 1, 0]
print(Evaluation.confusionMatrix_binary(y_pred,y_true))