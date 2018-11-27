import numpy as np

def minSquare(tuples):
    p1 = q1 = r1 = 0
    p2 = q2 = r2 = 0
    for x, y in tuples:
        # print('x: {0:<4}   y: {1:<4}'.format(x,y))
        p1 += x*x
        q1 += x
        r1 += x*y
        p2 += x
        q2 += 1
        r2 += y
    res = np.linalg.solve(np.array([[p1,q1], [p2,q2]]), np.array([r1,r2]))
    return res

