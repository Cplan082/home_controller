# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:18:09 2024

@author: clive
"""

def map_value(value, old_min, old_max, new_min, new_max):
    """
    Map a value from one range to another using linear mapping.

    Parameters:
    - value: The original value to be mapped.
    - old_min: The minimum value of the original range.
    - old_max: The maximum value of the original range.
    - new_min: The minimum value of the desired range.
    - new_max: The maximum value of the desired range.

    Returns:
    The mapped value in the new range.
    """
    old_range = old_max - old_min
    new_range = new_max - new_min

    # Perform linear mapping
    new_value = ((value - old_min) / old_range) * new_range + new_min

    return new_value