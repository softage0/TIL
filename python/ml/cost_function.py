import tensorflow as tf
import matplotlib.pyplot as plt

W = tf.placeholder(tf.float32)
b = tf.Variable(tf.random_normal([1]), name='bias')
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

sess = tf.Session()

sess.run(tf.global_variables_initializer())

W_val = []
b_val = []
cost_val = []

for i in range(-30, 50):
    feed_W = i * 0.1
    curr_cost, curr_W, curr_b = sess.run([cost, W, b],
                                         feed_dict={W: feed_W,
                                                    X: [1, 2, 3, 4, 5],
                                                    Y: [2.1, 3.1, 4.1, 5.1, 6.1]})

    W_val.append(curr_W)
    b_val.append(curr_b)
    cost_val.append(curr_cost)

plt.plot(W_val, cost_val)
plt.show()
