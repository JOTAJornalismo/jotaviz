"""jotaviz - A collection of plotting functions and styles used at jota.info"""

import matplotlib as mpl
import pkg_resources

from .core import jotaviz_footnote, jotaviz_heading, jotaviz_save_to_file, jotaviz_hide_first_and_last_yticks, jotaviz_hide_first_and_last_xticks

__version__ = pkg_resources.require("jotaviz")[0].version
__author__ = 'Daniel Marcelino <daniel.marcelino@jota.info>'
__all__ = []