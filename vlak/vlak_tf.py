import tensorflow as tf
import src.vlak.createTestData as ctd
import random

def test_tf():
    sess = tf.Session()
    data = ctd.train_data_4_tf(startVelocityRange1=20, startVelocityRange2=100, startVelocityStep=20,
                               endVelocityRangeDelta=10, endVelocityStep=5,
                               coef_a=0.5, coef_b=0.5)
    # print(data)

    # create model
    c = random.random()
    # print("c: ", c)
    a = tf.Variable([c], dtype=tf.float32)
    b = tf.Variable([1-c], dtype=tf.float32)
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)
    linear_model = a * x + b * y

    # compare to expected result
    z = tf.placeholder(tf.float32)
    squared_deltas = tf.square(linear_model - z)
    loss = tf.reduce_sum(squared_deltas)

    #optimization
    optimizer = tf.train.GradientDescentOptimizer(0.000001)
    train = optimizer.minimize(loss)

    #run
    init = tf.global_variables_initializer()
    sess.run(init)

    print("start [a,b]", sess.run([a,b]))
    print("start loss", sess.run(loss, {x: data[0], y: data[1], z: data[2]}))
    for i in range(50000):
        sess.run(train, {x: data[0], y: data[1], z: data[2]})
        # print(sess.run([a,b]))

    print("end [a,b]", sess.run([a,b]))
    print("end loss",  sess.run(loss, {x: data[0], y: data[1], z: data[2]}))

    sess.close()