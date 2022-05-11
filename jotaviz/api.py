#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
import matplotlib as mpl
from matplotlib.path import Path
import types
from types import ModuleType
from . import dotify


_set = types.__builtins__["set"]

def get(key=False):
	params = mpl.rcParams
	return params[key] if key else dotify(params)

###
# `set` accepts a dictionary of properties,
# or a module containing a `style` function 
# that returns such a dictionary.
###
def set(obj, *args, **kwargs):
	if type(obj) == ModuleType:
		props = obj.style(*args, **kwargs)
	else:
		props = obj
	dotted = dotify(props)
	for key in dotted:
		val = dotted[key]
		try:
			mpl.rcParams[key] = val
		except: pass

DEFAULT_PARAMS = dict((k, v[0]) for k, v in 
	mpl.rcsetup.defaultParams.items())

def reset(params=DEFAULT_PARAMS):
	old_keys = mpl.rcParams.keys()
	set(params)
	new_keys = mpl.rcParams.keys()
	keys_to_del = list(_set(old_keys) - _set(new_keys))
	for key in keys_to_del: del mpl.rcParams[key]