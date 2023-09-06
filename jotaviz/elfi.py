#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['elfi']

import math

def elfi(data_list):
    """
    The ELFI is a simplified method for calculating the Ethnolinguistic 
    Fractionalization Index (ELFI) This is one form of what is commonly called 
    a "diversity index."
    
    Accepts a list of decimal percentages, which are used to calculate the index.
    
    Returns a decimal value as a floating point number.
    
    h3. Example usage
    
        >>> import jotaviz
        >> jotaviz.elfi([0.2, 0.5, 0.05, 0.25])
        0.64500000000000002
   
    """
    # Convert all the values to floats and test to make sure there aren't any strings in there
    try:
        data_list = map(float, data_list)
    except ValueError:
        raise ValueError('Input values should contain numbers, your first input contains something else')
    # Calculate the ELFI
    return 1 - sum([math.pow(i, 2) for i in data_list])