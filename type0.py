
from scipy.optimize import fsolve
from math import sin, cos, exp, sqrt
import matplotlib.pyplot as plt


# unknown theta_b , theta_c
# parameter K,L1,L2
# L1長L2短

#b為鰭片厚度
#w為寬度
def main0(k, L1, L2, b, w, h, Q):
    n_up = int(0.02/2/(L2+b))
    def Z_f(m, l):
        return (1 - exp(-2 * m * l)) / (1 + exp(-2 * m * l))


    def m_f(h, k, b):
        return sqrt((2 * h) / (k * b))

    def f(x):
        theta_b = float(x[0])

        m = m_f(h, k, b)
        A = b * w
        Z2 = Z_f(m, L1)


        equ1 = n_up *2* Z2 * k * m * A * theta_b - Q

        return [
            equ1
        ]

    result = fsolve(f, [10])
    return result


if __name__ == '__main__':

    vals = []

    tbs = []
    k = 200
    L1 = 0.03
    L2 = 0.001
    b = 0.001
    w = 0.02
    h = 20
    Q = 10
    print(main0(k, L1, L2, b, w, h, Q ))
    val=Q
    val_s='Q(w)'

    # for i in range(1000):
    #
    #     dval = val*10/1000*i
    #     print(dval)
    #
    #     vals.append(val+dval)
    #     tbs.append(main1(k , L1, L2, b, w, h, Q+dval)[0])
    #
    # plt.plot(vals, tbs)
    # plt.xlabel(val_s)
    # plt.ylabel('theta_B(C)')
    # plt.show()