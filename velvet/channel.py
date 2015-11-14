"""Channel Module
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

__all__ = ['awgn']

import numpy as np
from .validation import assert_ndarray, assert_one_dimension

def awgn(v, snr, sigpower=None):
    """
    Additive white Gaussian noise.

    y = awgn(v, snr) adds white Gaussian noise to the signal v. The parameter,
    snr, specifies the signal-to-noise ratio in dB. The snr value is added
    on a per sample basis. If v, is complex then complex noise is added. 
    The power of v is measured before adding noise.
  
    y = awgn(..., sigpower) uses the value in sigpower as the signal power
    instead of measuring the data. The units of sigpower are dBW.

    Parameters
    -----------
    v : ndarray, scalar or complex
        Signal samples
        
    snr : float
        Signal-to-noise ratio per sample, in dB

    sigpower : float
        Signal power, in dBW

    Returns
    -------
    y : ndarray, scalar or complex
        Signal plus noise

    Notes
    ------
    This function uses signal-to-noise ratio (SNR) per sample. The
    signal-to-noise ratio is related to the energy per symbol to noise density
    ratio as 

    Es / No = (W / R) * S / N

    where S is the signal power, W is the noise bandwidth, R is the symbol rate and 
    N is the noise power.

    Examples
    ---------
    >>> import numpy as np
    >>> import velvet as vt
    >>> import matplotlib.pyplot as plt

    >>> y = np.sin(2*np.pi*100*np.arange(100)/10000);
    >>> ynoise = vt.awgn(y, 10.0);
    >>> plt.plot(y,'r');
    >>> plt.plot(ynoise,'b');
    >>> plt.grid('on')
    >>> plt.show()
    """
    # Input error checking
    assert_ndarray(v)
    assert_one_dimension(v)

    N = len(v)
    # If the signal power is not specified, we measure it
    if sigpower is None:
        sigPower = sum(abs(v)**2) / N
        sigPower = 10.0*np.log10(sigPower)
    else:
        sigPower = sigpower

    noisePower = sigPower - snr
    noiseVar = 10**(noisePower/10.0)
  
    if all(np.isreal(v)):
        noise = np.sqrt(noiseVar)*np.random.randn(N)
    else:
        noise = np.sqrt(noiseVar/2.0)*np.random.randn(N) + \
            1j*np.sqrt(noiseVar/2.0)*np.random.randn(N)

    return v + noise
