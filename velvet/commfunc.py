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
__all__ = ['berawgn', 'biterr', 'qfunc'] 

def berawgn(EbNodB, mod_type, M, mod_index=None, Kmin=None):
    """
    Bit error rate (BER) for additive white Gaussian noise channels

    ber = berawgn(EbNodB, mod_type, M) returns the theoretical BER of various
    modulation types over an additive white Gaussian noise channel. The
    input, EbNodb, is the bit energy to noise power spectral density
    ratio in dB. mod_type corresponds to the modulation type and M
    is the modulation alphabet size. 

    ber = berawgn(EbNodB, 'cpfsk', M, mod_index, Kmin) returns a lower
    bound on the BER for Continuous Phase Frequency Shift Keying (CPFSK).
    mod_index and Kmin specifiy the modulation index and the number
    of paths having the minimum distance, respectively. If the number
    of minimum distance paths is unknown, then a value of Kmin = 1
    is appropriate.
    
    The supported modulations are listed in the following table.

    =====================  ==========   ============    ==========
    Modulation Scheme      mod_type     Range of M      Encoding
    =====================  ==========   ============    ==========
    CPFSK                  'cpfsk'      Power of 2      N/A
    =====================  ==========   ============    ==========


    Parameters
    -----------
    EbNodB : {scalar, ndarray}
             Ratio of bit energy to noise power spectral density, in dB
        
    mod_type : string
              Modulation type. Refer to table for accepted values

    M : int
        Modulation alphabet size

    mod_index : float
        Modulation index for CPFSK

    Kmin : int
        Number of paths having the minimum distance


    Returns
    -------
    ber : {scalar, ndarray}
          The theoretical bit error rate

    References
    -----------
    .. [1] Proakis, J.G., Digital Communications, 4th ed., McGraw-Hill, 2001.

    Examples
    ---------
    >>> import velvet as vt
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np

    >>> EbNodB = np.arange(0,16.)
    >>> ber_cpfsk = kpi.berawgn(EbNodB,'cpfsk', 4, 0.5, 1)
    >>> plt.semilogy(EbNodB,ber_cpfsk);
    >>> plt.grid('on')
    >>> plt.xlabel(r'$\\frac{E_b}{N_0}$')
    >>> plt.ylabel(r'$P_e$')
    >>> plt.legend(('4-CPFSK'))
    >>> plt.show()

    """

    # Convert from dB to linear scale
    EbNoLin = 10**(EbNodB/10.0)

    mod_type = str.lower(mod_type)

    if mod_type == 'cpfsk':
        if mod_index is None or Kmin is None:
            raise ValueError("Values for mod_index and Kmin are required")
        k = np.arange(1, M)
        db2 = min((2.0 * np.log2(M)) * (1 - np.sinc(2*k*mod_index)))
        Pm = Kmin * qfunc(np.sqrt(EbNoLin * db2))
        ber = Pm / np.log2(M)
    else:
        raise ValueError("Modulation type must bet one of {'cpfsk'}")
      
    return ber


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
