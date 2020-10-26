from scipy.optimize import fsolve
from math import sin, cos, exp, sqrt
import matplotlib.pyplot as plt


# unknown theta_b , theta_c
# L1,Long
# L2,connect
# parameter K,L1,L2,h,b,w
def main2(k, L1, L2, h, b, w, Q,n):
    n_up = int(0.02/2 / (L2 + b))
    n=n-2

    m = m_f(h, k, b)
    X2 = X_f(m, L2)
    Y2 = Y_f(m, L2)
    Z2 = Z_f(m, L2)
    Z1 = Z_f(m, L1)

    def f(x):
        theta_z_unknown = float(x[0])
        theta_b,theta_c = theta_b_theta_c_f(theta_z_unknown,n,X2,Y2,Z1,Z2)
        Qb = X2*k*m*w*b*theta_b-Y2*k*m*w*b*theta_c
        Q_total = 2*Qb+n_up*2*Z1*k*m*w*b*theta_b
        equ1 = Q_total - Q
        return [
            equ1
        ]

    theta_z_unknown = 10
    theta_z = fsolve(f, [theta_z_unknown])

    theta_b, theta_c = theta_b_theta_c_f(theta_z, n, X2, Y2, Z1, Z2)

    return theta_b


def Z_f(m, l):
    return (1 - exp(-2 * m * l)) / (1 + exp(-2 * m * l))


def Y_f(m, l):
    return (2 * exp(-1 * m * l)) / (1 - exp(-2 * m * l))


def X_f(m, l):
    return (1 + exp(-2 * m * l)) / (1 - exp(-2 * m * l))


def m_f(h, k, b):
    return sqrt((2 * h) / (k * b))


def theta_zm1_f(theta_z, X, Y, Z1, Z2):
    return (X + 2 * Z1 + Z2) / Y * theta_z


def theta_zm2_f(theta_zm1, theta_z, X, Y, Z):
    return (2 * X + 2 * Z) / Y * theta_zm1 - theta_z


def theta_b_theta_c_f(theta_z, n, X, Y, Z1, Z2):
    theta_zm1 = theta_zm1_f(theta_z, X, Y, Z1, Z2)
    theta_zm2 = theta_zm2_f(theta_zm1, theta_z, X, Y, Z1)

    theta_z_i = theta_z
    theta_zm1_i = theta_zm1
    theta_zm2_i = theta_zm2

    for i in range(n):
        theta_z_i = theta_zm1_i
        theta_zm1_i = theta_zm2_i
        theta_zm2_i = theta_zm2_f(theta_zm1_i, theta_z_i, X, Y, Z2)

    theta_b = theta_zm2_i
    theta_c = theta_zm1_i
    return theta_b, theta_c

#
# def sovle_tb(k, L1, L2, b, w, h, Q):
#     def Z_f(m, l):
#         return (1 - exp(-2 * m * l)) / (1 + exp(-2 * m * l))
#
#     def Y_f(m, l):
#         return (2 * exp(-1 * m * l)) / (1 - exp(-2 * m * l))
#
#     def X_f(m, l):
#         return (1 + exp(-2 * m * l)) / (1 - exp(-2 * m * l))
#
#     def m_f(h, k, b):
#         return sqrt((2 * h) / (k * b))
#
#     def f(x):
#         theta_b = float(x[0])
#
#         m = m_f(h, k, b)
#         A = b * w
#         Z2 = Z_f(m, L1)
#         Z3 = Z_f(m, L2)
#         Y = Y_f(m, L2)
#         X = X_f(m, L2)
#
#         theta_c = Y / (X + 2 * Z2 + Z3) * theta_b
#         Qb = X * k * m * A * theta_b - Y * k * m * A * theta_c
#         equ1 = 2 * Qb + 2 * Z2 * k * m * A * theta_b - Q
#
#         return [
#             equ1
#         ]
#
#     result = fsolve(f, [10])
#     return result


if __name__ == '__main__':

    # vals = []
    #
    # tbs = []
    k = 200
    L1 = 0.03
    L2 = 0.01
    b = 0.001
    w = 0.02
    h = 20
    Q = 10
    #
    # val = Q
    # val_s = 'Q(w)'
    #
    # for i in range(1000):
    #     dval = val * 10 / 1000 * i
    #     print(dval)
    #
    #     vals.append(val + dval)
    #     tbs.append(sovle_tb(k, L1, L2, b, w, h, Q + dval)[0])
    #
    # plt.plot(vals, tbs)
    # plt.xlabel(val_s)
    # plt.ylabel('theta_B(C)')
    # plt.show()
    print(main2(k, L1, L2, h, b, w, Q,2))