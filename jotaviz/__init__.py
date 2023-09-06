#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""jotaviz - A collection of plotting functions and styles used at jota.info"""


try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata
package_name = "jotaviz"
__version__ = importlib_metadata.version(package_name)


from jotaviz.utils import *
from jotaviz.pizza import *
from jotaviz.bumpy import *
from jotaviz.radar import *
from jotaviz.quiver import *
from jotaviz.styles import *
from jotaviz.colors import *