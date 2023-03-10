"""Plot examples of ExtensysPlots style."""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import jotaviz

from utils import is_exist_dir, make_patch_spines_invisible

def test_plotting_working():
    plt.style.use("jotaviz")
    values = {c: [random.randint(0, 10) for _ in range(7)] for c in 'ABCDEF'}
    df = pd.DataFrame(values)

    df.plot(marker='o')
    jotaviz.jotaviz_footnote()

    plt.savefig("figures/test.png")



def g(x, m, L=1.0):
    return (np.cosh(m*(L-x))) / np.cosh(m*L)


save_dir = os.path.join(os.path.dirname(__file__), 'figures')
is_exist_dir(save_dir)

pparams = dict(xlabel='Fractional distance into pore, $x/L$', ylabel='Concentration $(mol.dm^{-3})$')

x = np.linspace(0, 1, 301)


with plt.style.context(['jotaviz']):
    fig, ax = plt.subplots()

    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig1'.format(save_dir), dpi=300)


with plt.style.context(['jotawhite']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig2'.format(save_dir), dpi=300)


with plt.style.context(['jotablack']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig3'.format(save_dir), dpi=300)
    
    
with plt.style.context(['jotadark']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig5'.format(save_dir), dpi=300)



with plt.style.context(['jotavoid']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig7'.format(save_dir), dpi=300)



import numpy as np
import matplotlib.pyplot as plt


def symmetric_limits(data):
    lim = max(-data.min(), data.max())
    return {'vmin': -lim, 'vmax': lim}


def case1_single_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [3, 2, 4, 1, 1]
    plt.plot(x, y)
    plt.show()


def case2_multi_line_plot():
    x = [1, 2, 3, 4, 5]
    y1 = [3, 2, 4, 1, 1]
    y2 = [4, 1, 3, 2, 0]
    y3 = [4.2, 0.8, 2, 2, 1]
    lines = plt.plot(x, y1, x, y2, x, y3)
    plt.legend(lines, ['y1', 'y2', 'y3'])
    plt.show()


def case3_filled_contours():
    x, y = np.mgrid[-3:3:50j, -3:3:50j]
    g = np.exp(-0.5*(x**2 + y**2)) - 1.3*np.exp(-0.5*(x**2 + 2*y**2))
    plt.contourf(x, y, g, **symmetric_limits(g))
    plt.show()


def case4_pseudocolor():
    x, y = np.mgrid[-3:3:50j, -3:3:50j]
    g = np.exp(-0.5*(x**2 + y**2)) - 1.3*np.exp(-0.5*(x**2 + 2*y**2))
    plt.pcolor(x, y, g, **symmetric_limits(g))
    plt.show()


def case5_single_boxplot():
    x = [1, 5, 5.1, 5.1, 5.5, 5.4, 5.5, 5.4, 5.6, 5.7, 6., 6.1, 9]
    plt.boxplot(x)
    plt.show()


if __name__ == '__main__':
    plt.style.use('jotaviz')
    # plt.style.use(['jotaviz', 'grayscale'])
    # case1_single_line_plot()
    # case2_multi_line_plot()
    # case3_filled_contours()
    # case4_pseudocolor()
    case5_single_boxplot()