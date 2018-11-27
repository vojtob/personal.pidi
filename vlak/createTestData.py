import random
import json
import numpy as np

def float_range(start, end, step):
    while start <= end:
        yield start
        start += step

# create test data, only velocity
def crete_test_data_velocity(startVelocityRange1=20, startVelocityRange2=100, startVelocityStep=10,
                    endVelocityRangeDelta=10, endVelocityStep=2,
                    coef_a=0.5, coef_b=0.5):
    for startVelocity in float_range(startVelocityRange1, startVelocityRange2, startVelocityStep):
        for endVelocity in float_range(startVelocity, startVelocity + endVelocityRangeDelta, endVelocityStep):
            error = 1- (random.random() - 0.5)/100.0
            # error = 1
            average_velocity = error * (coef_a * startVelocity + coef_b * endVelocity)
            rec = (startVelocity, endVelocity, average_velocity)
            yield rec

def binary2number(binaryNumber):
    result = 0
    i = 512
    for x in binaryNumber:
        # print(x)
        # print(x[0])
        if x[0] > 0.5: result += i
        i = i/2
    return result

def number2binary(n):
    return list('{0:010b}'.format(round(n)))
    result = 0
    i = 512
    for x in response:
        # print(x)
        # print(x[0])
        if x[0] > 0.5: result += i
        i = i/2
    return result

def train_data_4_net(startVelocityRange1=20, startVelocityRange2=100, startVelocityStep=10,
                    endVelocityRangeDelta=10, endVelocityStep=2,
                    coef_a=0.5, coef_b=0.5):
    train_data = []
    for item in crete_test_data_velocity(startVelocityRange1, startVelocityRange2, startVelocityStep,
                                         endVelocityRangeDelta, endVelocityStep,
                                         coef_a, coef_b):
        input_data = np.array([[item[0] / 100], [item[1] / 100]])
        # print(input_data)
        output_data = np.array([[int(x)] for x in number2binary(item[2] * 10)])
        # print(output_data)
        train_data.append((input_data, output_data))
    return train_data

def train_data_4_tf(startVelocityRange1=20, startVelocityRange2=100, startVelocityStep=10,
                    endVelocityRangeDelta=10, endVelocityStep=2,
                    coef_a=0.5, coef_b=0.5):
    x = []
    y = []
    z = []
    for item in crete_test_data_velocity(startVelocityRange1, startVelocityRange2, startVelocityStep,
                                         endVelocityRangeDelta, endVelocityStep,
                                         coef_a, coef_b):
        x.append(item[0])
        y.append(item[1])
        z.append(item[2])
    return (x,y,z)

def train_data_4_tf_simple(startVelocityRange1=20, startVelocityRange2=100, startVelocityStep=10,
                    endVelocityRangeDelta=10, endVelocityStep=2,
                    coef_a=0.5, coef_b=0.5):
    x = []
    y = []
    z = []
    x.append(20)
    y.append(30)
    z.append(35)
    return (x,y,z)

# write test data
def write_test_data(data):
    with open("vlak.json", 'w') as f:
        for item in data:
            f.write(json.dumps(item))
            f.write('\n')
