import tensorflow as tf

x = [[1., 2.],
     [3., 4.],
     [5., 6.]]

with tf.Session() as sess:
    print(tf.stack(x, axis=-1).eval())
