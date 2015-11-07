"""Utility Functions
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

import numpy as np

# Public API
__all__ = ['isodd']



def isodd(x):
    """ Check if a number is odd

    b = isodd(x) returns 1 (True) if x is odd, otherwise it returns 0
    (False).
    
    If x is a ndarray then b is an ndarray with each element
    set to 0 or 1, correspdonding to the value in each element of x.

    Parameters
    -----------
    x : {scalar, ndarray} : int value
        Input data

    Returns
    --------
    b : {scalar, ndarray}

    Examples
    ---------
    >>> import numpy as np
    >>> import velvet as vt
    >>> x = np.array([1,2,3])
    >>> vt.isodd(x)
    array([ 1,  0,  1])
   
    """

    # Error check input
    if isinstance(x, np.ndarray):
        if x.dtype != int:
            raise ValueError("input array must have int values") 
    elif not isinstance(x, int):
            raise ValueError("input must be an int") 


    return x & 1
