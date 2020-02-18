import Metrics

y_true = [0, 1, 2, 0, 1, 2,2,2,2,2]
y_pred = [0, 2, 1, 0, 0, 1,2,1,1,2]
print('Accuracy:', Metrics.accuracy(y_true, y_pred,True))
print('Recall:',Metrics.recall(y_true, y_pred))
print('precision:',Metrics.precision(y_true, y_pred))
print('f1_score:',Metrics.f1Score(y_true, y_pred))

actual_labels = ["bam", "ham", "spam"]
y_pred = [[0.8, 0.1, 0.1], [0.3, 0.6, 0.1], [0.15, 0.15, 0.7]]
print('logLoss:', Metrics.logLoss(actual_labels, y_pred))