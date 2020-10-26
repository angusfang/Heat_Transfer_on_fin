import type0, type1, type2
import plot_device
import matplotlib.pyplot as plt
import numpy as np

# chip 0.02m*0.02m
chip_L = 0.02
chip_W = 0.02
source_h = 0.01


def main(k, L1, L2, b, w, h, Q, n, plot=False):
    n_up = int(chip_L / 2 / (L2 + b))
    the_b = 0
    if n == 0:
        the_b = type0.main0(k, L1, L2, b, w, h, Q)
    if n == 1:
        the_b = type1.main1(k, L1, L2, b, w, h, Q)
    if n >= 2:
        the_b = type2.main2(k, L1, L2, h, b, w, Q, n)
    if plot == True:
        plot_device.plot_type2(chip_L, source_h, L1, L2, b, n, n_up)

    return the_b


if __name__ == '__main__':
    k = 238
    L1 = 0.03
    L2 = 0.001
    b = 0.001
    w = chip_W
    h = 20
    Q = 10
    n = 0

    val_b = np.linspace(0.0005, 0.0025, 10)

    val_k = np.array([237, 315, 398, 80.2, 411])
    val_density = np.array([2.7, 19.3, 8.92, 7.874, 10.49]) * 1000
    val_money = np.array([53.82, 1454000, 181.51, 7.5, 16667])
    val_name = ['Al', 'Au', 'Cu', 'Fe', 'Ag']

    val_L1 = np.linspace(0.015, 0.075, 10)
    val_L2 = np.linspace(0.0005, 0.0025, 10)
    val_n = np.array([0, 1, 2, 3, 4, 5])

    no = 0

    eles=np.array([ ])

    for bi in val_b:
        for i in range(5):
            for L1i in val_L1:
                for L2i in val_L2:
                    for ni in val_n:
                        n_up = int(0.02 / 2 / (L2i + bi))

                        volume = 0
                        volume1 = chip_L * bi * chip_W
                        volume2 = 2 * n_up * bi * L1i * chip_W
                        if ni == 0:
                            volume = volume1 + volume2
                        if ni != 0:
                            volumeb = volume1 + volume2
                            volume3 = ni * bi * (2 * L1i + bi) * chip_W
                            volume4 = (ni + 1) * L2i * bi * chip_W
                            volume5 = 2*(volume3+volume4)
                            volume = volumeb+volume5
                        mass = volume * val_density[i]
                        money = mass * val_money[i]
                        the_b = main(val_k[i],L1i,L2i,bi,w,h,Q,ni)[0]
                        ele = np.array([no,bi,i,L1i,L2i,ni,volume,mass,money,the_b])

                        if no ==0:
                            eles=ele
                        else:
                            eles = np.vstack([eles,ele])



                        print(no)
                        no = no + 1
        np.save('eles',eles)
print()
print()
print()
    # vals = []
    # tbs = []
    #
    # for i in range(10):
    #     dval = i
    #
    #     vals.append(i)
    #     tbs.append(main(k, L1, L2, b, w, h, Q, i)[0])
    #
    # # -lim
    # print(main(k, L1, L2, b, w, h, Q, 0, True))
    # # +lim
    # print(main(k, L1, L2, b, w, h, Q, 10, True))
    #
    # plt.plot(vals, tbs)
    # plt.xlabel(val_s)
    # plt.ylabel('theta_B(C)')
    # plt.show()
