"""Plot examples of ExtensysPlots style."""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import is_exist_dir, make_patch_spines_invisible


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


with plt.style.context(['jotaviz-white']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig2'.format(save_dir), dpi=300)


with plt.style.context(['jotaviz-black']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig3'.format(save_dir), dpi=300)
    
    
with plt.style.context(['jotaviz', 'dark_background']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
        ax.set(**pparams)
        ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    plt.savefig('{}/fig5'.format(save_dir), dpi=300)