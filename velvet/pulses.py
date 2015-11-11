"""Pulse shaping functions
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

import numpy as np

__all__ = ['rectpulse']



def rectpulse(L, fsT, normalize = True):
    """ Rectangular Pulse.

    u = rectpulse(L, fsT) generates a rectangular pulse spanning
    L symbol periods with fsT samples per symbol. The resulting pulse has length
    L * fsT.
    
    u = rectpulse(..., normalize) where normalize is one of {False, True}
    normalizes the pulse such that the maximum cummulative sum is equal to 1/2.
    If the pulse is being used for CPM then normalize should be set to
    True.

    Parameters
    -----------
    L : int
        Pulse length, in symbol intervals

    fsT : int
        Samples per symbol

    normalize : boolean
        True of False, default is True

    Returns
    --------
    u : ndarray of float values
        Pulse samples

    Examples
    ---------
    >>> import velvet as vt
    >>> u = vt.pulse(1, 4)
    >>> print u
    [ 0.125  0.125  0.125  0.125]

    """
    u = np.ones(L * fsT, dtype='float')

    # Normalize so that the integral of the pulse is 1/2 max
    if normalize:
        u = u / (2.0 * np.sum(u))
  
    return u
