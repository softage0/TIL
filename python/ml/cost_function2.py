import tensorflow as tf
import matplotlib.pyplot as plt

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

learning_rate = 0.1
gradient = tf.reduce_mean((W * X - Y) * X)
descent = W - learning_rate * gradient
update = W.assign(descent)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

feed_dict = {X: [1, 2, 3, 4, 5],
             Y: [2.1, 3.1, 4.1, 5.1, 6.1]}
W_val = []
step_val = []
cost_val = []

for step in range(21):
    sess.run(update, feed_dict=feed_dict)
    step_val.append(step)
    cost_val.append(sess.run(cost, feed_dict=feed_dict))
    W_val.append(sess.run(W))

plt.plot(step_val, cost_val)
plt.plot(step_val, W_val)
plt.show()
