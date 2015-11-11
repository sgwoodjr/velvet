"""Utility Functions
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

from __future__ import print_function
import sys
import numpy as np

# Public API
__all__ = ['isodd', 'ProgressBar']



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

class ProgressBar: 
    """Print a progress bar to the terminal

    Code grabbed from an Ipython Notebook example.

    Example useage:
    P = ProgressBar(10)
    for ii in arange(10):
        p.animate(ii+1)
    """

    def __init__(self, iterations):
        self.iterations = iterations
        self.prog_bar = '[]'
        self.fill_char = '*'
        self.width = 50
        self.__update_amount(0)

    def animate(self, iter):
        print('\r', self, end=' ')
        sys.stdout.flush()
        self.update_iteration(iter + 1)

    def update_iteration(self, elapsed_iter):
        self.__update_amount((elapsed_iter / float(self.iterations)) * 100.0)
        self.prog_bar += '  %d of %s complete' % (elapsed_iter, self.iterations)

    def __update_amount(self, new_amount):
        percent_done = int(round((new_amount / 100.0) * 100.0))
        all_full = self.width - 2
        num_hashes = int(round((percent_done / 100.0) * all_full))
        self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        pct_place = (len(self.prog_bar) // 2) - len(str(percent_done))
        pct_string = '%d%%' % percent_done
        self.prog_bar = self.prog_bar[0:pct_place] + \
            (pct_string + self.prog_bar[pct_place + len(pct_string):])

    def __str__(self):
        return str(self.prog_bar)
