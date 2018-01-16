import tensorflow as tf
import numpy as np

xy = np.loadtxt('../../DeepLearningZeroToAll/data-01-test-score.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data.shape)
print(y_data.shape)
print(x_data[1][2])
