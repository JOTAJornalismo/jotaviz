#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Python module containing helper functions for jotaviz."""

from tempfile import NamedTemporaryFile
from urllib.request import urlopen

import matplotlib as mpl
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
from PIL import Image
import sys
import os
import shutil
from typing import Union


__all__ = ['add_image', 'validate_ax', 'set_visible', 'FontManager', 'set_labels', 'remove_na', 'sex_symbol', 'dollar_format', 'real_format', 'currency_format']


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
    >>> from jotaviz import add_image
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

    @classmethod
    def init_font_manager(cls):
        # Linux
        if sys.platform.startswith("linux"):
            try:
                if not os.path.isdir(os.path.expanduser('~/.fonts/')):
                    os.mkdir(os.path.expanduser('~/.fonts/'))
                return True
            except Exception as err:
                sys.stderr.write("FontManager error: " + str(err) + "\n")
                return False

        # other platforms
        else:
            return True

    @classmethod
    def windows_load_font(cls, font_path: Union[str, bytes], private: bool = True, enumerable: bool = False) -> bool:
        """ Function taken from: https://stackoverflow.com/questions/11993290/truly-custom-font-in-tkinter/30631309#30631309 """

        from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20

        if isinstance(font_path, bytes):
            path_buffer = create_string_buffer(font_path)
            add_font_resource_ex = windll.gdi32.AddFontResourceExA
        elif isinstance(font_path, str):
            path_buffer = create_unicode_buffer(font_path)
            add_font_resource_ex = windll.gdi32.AddFontResourceExW
        else:
            raise TypeError('font_path must be of type bytes or str')

        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        num_fonts_added = add_font_resource_ex(byref(path_buffer), flags, 0)
        return bool(num_fonts_added)

    @classmethod
    def load_font(cls, font_path: str) -> bool:
        # Windows
        if sys.platform.startswith("win"):
            return cls.windows_load_font(font_path, private=True, enumerable=False)

        # Linux
        elif sys.platform.startswith("linux"):
            try:
                shutil.copy(font_path, os.path.expanduser("~/.fonts/"))
                return True
            except Exception as err:
                sys.stderr.write("FontManager error: " + str(err) + "\n")
                return False

        # macOS and others
        else:
            return False


def remove_na(vector):
    """Helper method for removing null values from data vectors.
    Parameters
    ----------
    vector : vector object
        Must implement boolean masking with [] subscript syntax.
    Returns
    -------
    clean_clean : same type as ``vector``
        Vector of data with null values removed. May be a copy or a view.
    """
    return vector[pd.notnull(vector)]



def sex_symbol(is_female):
    if is_female:
        return "♀"
    else:
        return "♂"



def dollar_format(suffix=""):
    """Dollar formatter for matplotlib.
    :param suffix: Suffix to append, e.g. 'B'. Defaults to ''.
    :returns: FuncFormatter.
    """
    return currency_format(currency="USD", suffix=suffix)


def real_format(suffix=""):
    """Dollar formatter for matplotlib.
    :param suffix: Suffix to append, e.g. 'B'. Defaults to ''.
    :returns: FuncFormatter.
    """
    return currency_format(currency="BRL", suffix=suffix)


def currency_format(currency="BRL", suffix=""):
    """Currency formatter for matplotlib.
    :param currency: Name of the currency, e.g. 'USD', 'GBP', 'BRL', 'ARS'.
    :param suffix: Suffix to append, e.g. 'B'. Defaults to ''.
    :returns: FuncFormatter.
    """

    prefix = {"BRL": "R$", "USD": "$", "GBP": "£", "ARS": "$"}[currency]

    return mpl.ticker.FuncFormatter(
        lambda x, _: prefix + format(int(x), ",") + suffix
    )