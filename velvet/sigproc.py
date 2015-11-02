"""Signal processing functions
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

import numpy as np
from .validation import assert_ndarray, assert_one_dimension

fft = np.fft.fft
ifft = np.fft.ifft

# Public API
__all__ = ['conv', 'nextpower2', 'upsample']

def conv(x, h):
    """ Linear convolution.

    c = conv(x, h) returns the linear convolution between x and h.

    The output array, c, has length L = N + M - 1, where 
    N is the length of x and M is the length of h.

    Parameters
    -----------
    x : ndarray
        Input sequence

    h : ndarray
        Input sequence

    Returns
    --------
    c : ndarray
        Convolution sequence

    See Also
    ---------

    Notes
    ------
    Convolution in time, x(t) * h(t), is equivalent to multiplication in
    the frequency domain, X(f) H(f). The frequency domain transformation
    and multiplication is more efficient (faster) than convolving in time.

    References
    -----------
    .. [1] Wikipedia, "Convolution", http://en.wikipedia.org/wiki/Convolution


    Examples
    ---------
    >>> import numpy as np
    >>> import velvet as vt
    >>> x = np.array([1,2,3])
    >>> h = np.array([0,1,0.5])
    >>> vt.conv(x, h)
    array([  7.49400542e-16,   1.00000000e+00,   2.50000000e+00,
        4.00000000e+00,   1.50000000e+00])

    """

    # Input error checking
    assert_ndarray(x)
    assert_ndarray(h)
    assert_one_dimension(x)
    assert_one_dimension(h)

    N = len(x) + len(h) - 1

    # Compute FFT size
    p = nextpower2(2*N)
    fftSize = 2**p

    # Compute FFT of inputs
    X = fft(x,fftSize)
    H = fft(h,fftSize)

    # Actual convolution
    temp = ifft(X * H)

    # Remove values that result from FFT padding
    out = temp[0:N]

    # Should output be real or complex
    if x.dtype == 'complex' or h.dtype == 'complex':
        return out
    else:
        return np.real(out)


def nextpower2(x):
    """ Next power of 2.

    p = nextpower2(x) returns the first p such that 2**p is >= abs(x).

    Parameters
    -----------
    x : scalar
        Input value

    Returns
    --------
    p : scalar
        Next power 

    See Also
    ---------

    Notes
    ------

    References
    -----------

    Examples
    ---------
    >>> import velvet as vt
    >>> vt.nextpower2(513)
    10
    
    """
    temp = np.abs(x)
    v = int(np.ceil(np.log2(temp)))
    return v
 
def upsample(x, N):
    """Upsample data.

    y = upsample(x, N) upsamples the data in array x by factor N. Upsampling
    is accomplished by inserting N-1 zeros between each sample of x.

    Parameters
    -----------
    x : ndarray
        Input data

    N : int
        Upsample value

    Returns
    --------
    y : ndarray
        Upsampled data

    See Also
    ---------
    repeat

    Examples
    ---------
    >>> import numpy as np
    >>> import velvet as vt
    >>> x = np.array([1,2,3])
    >>> vt.upsample(x, 2)
    array([ 1,  0,  2,  0,  3,  0])
   
    """

    # Input error checking
    assert_ndarray(x)
    assert_one_dimension(x)

    y = np.zeros(N * len(x), dtype=x.dtype)

    jj = 0
    for ii in np.arange(len(x)):
        y[jj] = x[ii]
        jj += N

    return y
