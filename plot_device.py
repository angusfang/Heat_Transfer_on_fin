import matplotlib.pyplot as plt


def plot_square(l, h, x, y, color='k'):
    p1 = [l / 2.0, h / 2]
    p2 = [l / 2.0, -h / 2]
    p3 = [-l / 2.0, -h / 2]
    p4 = [-l / 2.0, h / 2]
    plt.plot([p1[0] + x, p2[0] + x], [p1[1] + y, p2[1] + y], c=color)
    plt.plot([p2[0] + x, p3[0] + x], [p2[1] + y, p3[1] + y], c=color)
    plt.plot([p3[0] + x, p4[0] + x], [p3[1] + y, p4[1] + y], c=color)
    plt.plot([p4[0] + x, p1[0] + x], [p4[1] + y, p1[1] + y], c=color)


def plot_source(l, h, x, y):
    plot_square(l, h, x, y, 'r')


def plot_base(l, h, x, y):
    plot_square(l, h, x, y, 'b')


def plot_fin_1(l, h, x, y, w, n):
    for i in range(n):
        plot_square(l, h, x + (i + 0.5) * (w + l), y, 'k')
        plot_square(l, h, -(x + (i + 0.5) * (w + l)), y, 'k')


def plot_fin_2(fin_t,fin_L, x, y, fin_L2, n):
    for i in range(n):
        plot_square(fin_t, fin_L, x + (i + 0.5) * (fin_L2 + fin_t), y, 'g')
        plot_square(fin_t, fin_L, -(x + (i + 0.5) * (fin_L2 + fin_t)), y, 'g')

        plot_square(fin_t, fin_L, x + (i + 0.5) * (fin_L2 + fin_t), -y+fin_t, 'g')
        plot_square(fin_t, fin_L, -(x + (i + 0.5) * (fin_L2 + fin_t)), -y+fin_t, 'g')

        plot_square(fin_L2 , fin_t, x + i * (fin_L2 + fin_t), y-0.5*fin_L-0.5*fin_t, 'b')
        plot_square(fin_t , fin_t, x + i * (fin_L2 + fin_t)+0.5*fin_t+0.5*fin_L2, y-0.5*fin_L-0.5*fin_t, 'b')
        plot_square(fin_L2, fin_t, -x + -i * (fin_L2 + fin_t), y - 0.5 * fin_L - 0.5 * fin_t, 'b')
        plot_square(fin_t, fin_t, -x + -i * (fin_L2 + fin_t) - 0.5 * fin_t - 0.5 * fin_L2, y - 0.5 * fin_L - 0.5 * fin_t,
                    'b')
    if n>=1:
        plot_square(fin_L2, fin_t, x + n * (fin_L2 + fin_t), y - 0.5 * fin_L - 0.5 * fin_t, 'b')
        plot_square(fin_L2, fin_t, -x + -n * (fin_L2 + fin_t), y - 0.5 * fin_L - 0.5 * fin_t, 'b')

def plot_type2(sourse_l,sourse_h,fin_L,fin_L2,fin_t,n,n_up):
    base_h = fin_t
    plot_source(sourse_l, sourse_h, 0, -0.5 * sourse_h)
    plot_base(sourse_l, base_h, 0, 0.5 * base_h)
    plot_fin_1(fin_t, fin_L, 0, base_h + fin_L * 0.5, fin_L2, n_up)
    plot_fin_2(fin_t, fin_L, sourse_l / 2 + fin_L2 / 2, base_h + fin_L * 0.5, fin_L2, n)
    plt.xlim([0.1, -0.1])
    plt.ylim([-0.1, 0.1])
    plt.show()


if __name__ == '__main__':
    sourse_l = 2
    sourse_h = 1

    fin_L = 1.5
    fin_L2 = 0.06
    fin_t = 0.12

    n=3
    n_up=2
    plot_type2(sourse_l,sourse_h,fin_L,fin_L2,fin_t,n,n_up)
