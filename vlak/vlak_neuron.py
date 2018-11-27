import src.vlak.net
import src.vlak.createTestData as ctd
import numpy as np

def test_neuron():
    ca = 0.2
    cb = 1 - ca
    train_data = ctd.train_data_4_net(startVelocityRange1=20, startVelocityRange2=90, startVelocityStep=.5,
                                      endVelocityRangeDelta=10, endVelocityStep=.5,
                                      coef_a=ca, coef_b=cb)

    net = src.vlak.net.Network([2, 15, 15, 10])
    net.SGD(train_data, 10, 10, 3)

    for startVelocity in range(20, 100, 20):
        for endVelocity in range(startVelocity, startVelocity + 10, 2):
            average_velocity = (ca * startVelocity + cb * endVelocity)
            input_data = np.array([[startVelocity / 100], [endVelocity / 100]])
            response = net.feedforward(input_data)
            cauculated_velocity = ctd.binary2number(response) / 10
            print('{:6.1f} {:6.1f} {:6.1f} {:6.1f} {:8.3f}'.format(startVelocity, endVelocity, average_velocity,
                                                                   cauculated_velocity, 100 * abs(
                    cauculated_velocity - average_velocity) / average_velocity))
