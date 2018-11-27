import numpy as np
import src.vlak.createTestData as ctd

'''
x - startVelocity
y - endVelocity
z - dlzka / doba

ax + by = dlzka / doba

Metodou najmensich stvorcov chcem najst a,b take aby funkcia g bola minimalna 
g = (ax+by-z)**2
derivovanim
dg / da = 2x(ax+by-z) = 2(x**2)a + 2xyb - 2xz
dg / db = 2x(ax+by-z) = 2xya + 2(y**2)b - 2yz

extrem je pre derivacie rovne 0, preto riesim sustavu
p1a + q1b = r1
p2a + q2b = r2
kde
p1 = x**2 
q1 = xy
r1 = xz
p2 = xy
q2 = y**2
r2 = yz
'''

def calc_Coef(a, b):
    p1 = q1 = r1 = 0.0
    p2 = q2 = r2 = 0.0
    for data in ctd.crete_test_data_velocity(coef_a=a, coef_b=b):
        x = data[0]
        y = data[1]
        z = data[2]
        p1 += x**2
        q1 += x*y
        r1 += x*z
        p2 += x*y
        q2 += y**2
        r2 += y*z

    res = np.linalg.solve(np.array([[p1,q1], [p2,q2]]), np.array([r1,r2]))
    # res = res * 3.6
    return res

def test_stvorce():
    print('{:>6} {:>6} {:>8} {:>8} {:>8} {:>8}'.format('a', 'b', 'calc a', 'calc b', 'err %', 'err %'))
    for a in ctd.float_range(0.1, 0.5, 0.1):
        b = 1 - a
        for i in range(1, 5):
            res = calc_Coef(a, b)
            print('{:6.2f} {:6.2f} {:8.4f} {:8.4f} {:8.4f} {:8.4f}'.format(a, b, res[0], res[1], 100*abs(a-res[0])/res[0], 100*abs(b-res[1])/res[1]))
