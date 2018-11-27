import minSquare
import matplotlib.pyplot as plt

# nacitanie suboru
def readData(fileName):
    tuples = []
    with open(fileName) as  f:
        for line in f:
            s = line.split('\t')
            # print(int(s[0]), int(s[1]))
            tuples.append([int(s[0]), int(s[1])])
    return tuples

# calc min square
tuples = readData('res/data.csv')
r = minSquare.minSquare(tuples)

def f(x):
    return r[0]*x + r[1]

def g(x):
    return -0.3*x + 7

#  draw graph
xval = []
yval = []
for x, y in tuples:
    xval.append(x)
    yval.append(y)

x1 = -30
y1 = f(x1)
x2 = 40
y2 = f(x2)
print('a: {0:<4}   b: {1:<4}'.format(r[0],r[1]))
print('x: {0:<4}   y: {1:<4}'.format(x1,y1))
print('x: {0:<4}   y: {1:<4}'.format(x2,y2))
print('**********')
z1 = g(x1)
z2 = g(x2)
print('x: {0:<4}   y: {1:<4}'.format(x1,z1))
print('x: {0:<4}   y: {1:<4}'.format(x2,z2))

calcx = []
calcy = []
for x in range(-30, 40):
    # print('x: {0:<4}   y: {1:<4}'.format(x, int(f(x))))
    calcx.append(x)
    calcy.append(int(f(x)))

plt.plot(xval, yval, 'bo')
plt.axis([-30, 40, 0, 14])
plt.show()
plt.plot(xval, yval, 'bo', [x1, x2], [y1, y2], 'r-')
plt.axis([-30, 40, 0, 14])
plt.show()
plt.plot(xval, yval, 'bo', [x1, x2], [z1, z2], 'r-')
plt.axis([-30, 40, 0, 14])
plt.show()
# plt.plot(xval, yval, 'bo', [x1, x2], [y1, y2], 'r-', calcx, calcy, 'g-')
# plt.show()
