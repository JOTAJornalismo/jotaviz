"""Plot examples of ExtensysPlots style."""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from examples.utils import is_exist_dir, make_patch_spines_invisible


def doplot():
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        ax.plot(x, np.sin(x + i * .5) * (7 - i))
    return ax


with plt.style.context(['jotaviz']):
    doplot()
    plt.savefig('{}/fig7'.format(save_dir), dpi=300)


with plt.style.context(['jotaviz-black']):
    doplot()
    plt.savefig('{}/fig1'.format(save_dir), dpi=300)


with plt.style.context(['jotaviz-white']):
    doplot()
    plt.savefig('{}/fig2'.format(save_dir), dpi=300)


with plt.style.context(['jotaviz-glass']):
    doplot()
    plt.savefig('{}/fig3'.format(save_dir), dpi=300)


with plt.style.context(['jotaviz', 'dark_background']):
    doplot()
    plt.savefig('{}/fig5'.format(save_dir), dpi=300)
