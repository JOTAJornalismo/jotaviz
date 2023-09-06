#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['jotaviz']


def median(data_list):
    """
    Accepts a list of numbers and returns the median value.
    
    The median is the number in the middle of a sequence, 
    with 50 percent of the values above, and 50 percent below.
    
    In cases where the sequence contains an even number of values -- and
    therefore no exact middle -- the two values nearest the middle
    are averaged and the mean returned.
    
    h3. Example usage
    
        >> import jotaviz
        >> seq1 = [1,2,3]
        >> jotaviz.median(seq1)
        2.0
        >> seq2 = (1,4,3,2)
        >> jotaviz.median(seq2)
        2.5
        
    h3. Documentation
    
        * "median":http://en.wikipedia.org/wiki/Median
    
    """
    # Convert all the values to floats and test to make sure there aren't any strings in there
    try:
        data_list = map(float, data_list)
    except TypeError:
        raise TypeError('Input values should be a number, your first input contains something else')
    # Fetch the total number of values
    n = len(data_list)
    # Sort the values from top to bottom
    data_list.sort()
    # Test whether the n is odd
    if n & 1:
        # If is is, get the index simply by dividing it in half
        index = n / 2
        median = data_list[index]
    else:
        # If the n is even, average the two values at the center
        low_index = (n / 2) - 1
        high_index = n / 2
        median = (data_list[low_index] + data_list[high_index]) / 2.0
    return median