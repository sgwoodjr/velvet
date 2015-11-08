"""Communication Module
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

import numpy as np
import scipy.special
from .validation import assert_ndarray, assert_one_dimension

erfc = scipy.special.erfc

# Public API
__all__ = ['biterr', 'qfunc'] 


def biterr(x, y):
    """
    Compute number of bit errors.

    n = biterr(x, y) returns the number of differences between the two arrays
    x and y, where each contains binary data. 

    Parameters
    -----------
    x : ndarray of ints
        Input array of binary data, {0, 1}

    y : ndarray of ints
        Input array of binary data, {0, 1}
        
    Returns
    -------
    n : int
        Number of errors

    Examples
    ---------
    >>> import numpy as np
    >>> import velvet as vt
    >>> x = np.array([0, 1, 1, 0])
    >>> y = np.array([1, 1, 0, 0])
    >>> vt.biterr(x, y)
    2
  
  """
    # Error checking
    assert_ndarray(x)
    assert_ndarray(y)
    assert_one_dimension(x)
    assert_one_dimension(y)
    if len(x) != len(y):
        raise ValueError("x and y must have same length")

    num_errors = 0
    for ii in np.arange(len(x)):
        if x[ii] != y[ii]:
            num_errors += 1

    return num_errors


def qfunc(x):
    """Compute the Q-function.

    Q = qfunc(x) computes the Q-function for x. 

    Parameters
    ------------
    x : {scalar, ndarray}
        A real number or an array of real numbers

    Returns
    -------
    Q : {scalar, ndarray}
        The Q-function

    Notes
    ------
    The Q-function is the tail probability of the standard normal distribution
    and is defined by

    .. math:: Q(x) = \\frac{1}{\sqrt{2 \pi}} \int_{x}^{\infty} \exp\left(-\\frac{t^2}{2}\\right) dt

    The tail probability is one minus the cummulative distribution function, so
    we also have

    .. math:: Q(x) = 1 - Q(-x) = 1 - \Phi(x)

    :math:`Q(x)` can also be written in terms of the complimentary error
    function

    .. math:: Q(x) = \\frac{1}{2} erfc\left(\\frac{x}{\sqrt{2}}\\right)


    Examples
    ---------
    >>> import numpy as np
    >>> import velvet as vt
    >>> x = np.array([0, 1, 2, 3])
    >>> vt.qfunc(x)
    array([ 0.5       ,  0.15865525,  0.02275013,  0.0013499 ])

    """
    # Error check inputs
    if isinstance(x, np.ndarray):
        if x.dtype == np.complex128:
            raise TypeError("complex input not supported")
    else:
        if isinstance(x, complex):
            raise TypeError("complex input not supported")

    Q = 0.5 * erfc(x / np.sqrt(2.0))
    return Q
