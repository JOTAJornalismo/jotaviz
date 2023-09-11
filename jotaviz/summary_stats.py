#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['summary_stats']

import jotaviz

def summary_stats(data_list):
    """
    Accepts a sample of numbers and returns a pretty
    print out of a variety of descriptive statistics.
    """
    mean = jotaviz.mean(data_list)
    median = jotaviz.median(data_list)
    mode = jotaviz.mode(data_list)
    n = len(data_list)
    max_ = max(data_list)
    min_ = min(data_list)
    range_ = jotaviz.range(data_list)
    standard_deviation = jotaviz.standard_deviation(data_list)
    
    print("""
    Summary statistics
    ==================
    
    n:        %s
    max:        %s
    min:        %s
    range:        %s
    mean:        %s
    median:        %s
    mode:        %s
    std:        %s
    """ % (n, max_, min_, range_, mean, median, mode, standard_deviation))