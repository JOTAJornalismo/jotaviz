#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Python module containing helper functions for jotaviz."""

from tempfile import NamedTemporaryFile
from urllib.request import urlopen

import matplotlib.font_manager as fm
import numpy as np
from PIL import Image


__all__ = ['add_image', 'validate_ax', 'set_visible', 'FontManager', 'set_labels']


def add_image(image, fig, left, bottom, width=None, height=None, **kwargs):
    """ Adds an image to a figure using fig.add_axes and ax.imshow

    If downsampling an image 'hamming' interpolation is recommended

    Parameters
    ----------
    image: array-like or PIL image
        The image data.
    fig: matplotlib.figure.Figure
        The figure on which to add the image.
    left, bottom: float
        The dimensions left, bottom of the new axes.
        All quantities are in fractions of figure width and height.
        This positions the image axis in the figure left% in from the figure side
        and bottom% in from the figure bottom.
    width, height: float, default None
        The width, height of the new axes.
        All quantities are in fractions of figure width and height.
        For best results use only one of these so the image is scaled appropriately.
    **kwargs : All other keyword arguments are passed on to matplotlib.axes.Axes.imshow.

    Returns
    -------
    matplotlib.axes.Axes

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from PIL import Image
    >>> from mplsoccer import add_image
    >>> from urllib.request import urlopen
    >>> fig, ax = plt.subplots()
    >>> image_url = 'https://upload.wikimedia.org/wikipedia/commons/b/b8/Messi_vs_Nigeria_2018.jpg'
    >>> image = urlopen(image_url)
    >>> image = Image.open(image)
    >>> ax_image = add_image(image, fig, left=0.1, bottom=0.2, width=0.4, height=0.4)
    """
    if isinstance(image, Image.Image):
        image_width, image_height = image.size
    else:
        image_height, image_width = image.shape[:2]

    image_aspect = image_width / image_height

    figsize = fig.get_size_inches()
    fig_aspect = figsize[0] / figsize[1]

    if height is None:
        height = width / image_aspect * fig_aspect

    if width is None:
        width = height * image_aspect / fig_aspect

    # add image
    ax_image = fig.add_axes((left, bottom, width, height))
    ax_image.axis('off')  # axis off so no labels/ ticks

    ax_image.imshow(image, **kwargs)

    return ax_image


def validate_ax(ax):
    """ Error message when ax is missing."""
    if ax is None:
        msg = "Missing 1 required argument: ax. A Matplotlib axis is required for plotting."
        raise TypeError(msg)


def set_visible(ax, spine_bottom=False, spine_top=False, spine_left=False, spine_right=False,
                grid=False, tick=False, label=False):
    """ Helper method to set the visibility of matplotlib spines, grid and ticks/ labels.
    By default sets all to invisible.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis to set visibility on.
    spine_bottom, spine_top, spine_left, spine_right : bool, default False
        Whether to show the spines.
    grid : bool, default False
        Whether to show the grid lines.
    tick : bool, deafult False
        Whether to draw the ticks.
    label : bool, default False
        Whether to draw the tick labels.
    """
    ax.spines['bottom'].set_visible(spine_bottom)
    ax.spines['top'].set_visible(spine_top)
    ax.spines['left'].set_visible(spine_left)
    ax.spines['right'].set_visible(spine_right)
    ax.grid(grid)
    ax.tick_params(bottom=tick, top=tick, left=tick, right=tick,
                   labelbottom=label, labeltop=label, labelleft=label, labelright=label)


def set_labels(ax, label_value, label_axis):
    """
    Function to set label for a given axis.

    Args:
        ax (axes.Axes): axis object.
        label_value (list): ticklabel values.
        label_axis (str): axis name, 'x' or 'y'

    Returns:
        list: label names
    """
    if label_axis == 'x':
        ax.set_xticks(np.arange(len(label_value)))
        axis = ax.get_xticklabels()
    else:
        ax.set_yticks(np.arange(len(label_value)) + 1)
        axis = ax.get_yticklabels()

    # fetch labels
    labels = [items.get_text() for items in axis]

    # init a count variable
    if label_axis == 'x':
        count = 0
    else:
        count = len(label_value) - 1

    # iterate through all the labels and change the label name
    for i in range(len(labels)):
        labels[i] = label_value[count]

        if label_axis == 'x':
            count += 1
        else:
            count -= 1

    return labels



class FontManager:
    """Utility to load fun fonts from https://fonts.google.com/ for matplotlib.
    Find a nice font at https://fonts.google.com/, and then get its corresponding URL
    from https://github.com/google/fonts/.


    The FontManager is taken from the ridge_map package by Colin Carroll (@colindcarroll).

    Parameters
    ----------
    url : str, default is the url for Roboto-Regular.ttf
        Can really be any .ttf file, but probably looks like
        'https://github.com/google/fonts/blob/main/ofl/cinzel/static/Cinzel-Regular.ttf?raw=true'
        Note make sure the ?raw=true is at the end.

    Examples
    --------
    >>> from mplsoccer import FontManager
    >>> import matplotlib.pyplot as plt
    >>> font_url = 'https://github.com/google/fonts/blob/main/ofl/abel/Abel-Regular.ttf?raw=true'
    >>> fm = FontManager(url=font_url)
    >>> fig, ax = plt.subplots()
    >>> ax.text(x=0.5, y=0.5, s="Good content.", fontproperties=fm.prop, size=30)
    """

    def __init__(self,
                 url=('https://github.com/google/fonts/blob/main/'
                      'apache/roboto/static/Roboto-Regular.ttf?raw=true')):
        self.url = url
        with NamedTemporaryFile(delete=False, suffix=".ttf") as temp_file:
            temp_file.write(urlopen(self.url).read())
            self._prop = fm.FontProperties(fname=temp_file.name)

    @property
    def prop(self):
        """Get matplotlib.font_manager.FontProperties object that sets the custom font."""
        return self._prop

    def __repr__(self):
        return f'{self.__class__.__name__}(font_url={self.url})'
