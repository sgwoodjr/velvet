""" CPM modulation Class
"""

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

import numpy as np
import scipy.signal
from .sigproc import upsample
from .validation import assert_ndarray, assert_one_dimension

lfilter = scipy.signal.lfilter

# Public API
__all__ = ['CPMMod']


class CPMMod(object):
    """
    Continuous Phase Modulation.

    The CPMMod class performs continuous phase modulation.

    mycpm = CPM(M, T, h, u, fsT) constructs a CPM modulator object with
    alphabet size M, modulation index h, frequency pulse u and fsT samples
    per symbol. 

    Parameters
    -----------
    M : int
        Alphabet size, must be a power of 2
                
    T : float
        Symbol rate, in seconds

    h : float
        Modulation index

    u : ndarray of floats
        Frequency pulse shape

    fsT : int
        Samples per symbol

    Returns
    -------
    v : ndarray of complex floats
        Modulation samples

    Notes
    ------
    For more details on the theory of CPM refer to [1]_.

    References
    -----------
    .. [1] Anderson, J., Aulin, T., Sundbergm C., Digital Phase Modulation,
    Plenum Press, 1986.


    Examples
    ---------
    >>> import velvet as vt
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt

    >>> cpm = vt.CPMMod(2, 1.0/2400, 0.5, np.ones(1,4), 4)
    >>> syms = 2 * np.random.randint(0, 2, 1000) - 1
    >>> v = cpm.mod(syms)
    
    """

    def __init__(self, M, Td, h, u, fsT):
        """
        Constructor
        """
        self._Mary = M
        self._symbol_period = Td
        self._mod_index = h
        self._pulse = u
        self._fsT = fsT

        # Normalize the pulse shape. It should integrate to 1/2.
        # Check the integration with: cumsum(pulse).
        self._pulse = self._pulse / np.sum(self._pulse) / 2.0

        # Phase is in radians
        self._phase_state = 0.0
        self._zinit = np.zeros(len(u) - 1, dtype='float')

        # The frequency deviation. Note that this is *not* the max
        # frequency deviation.
        self._freq_deviation = h / (2.0 * Td)

    @property
    def freq_deviation(self):
        """Frequency deviation"""
        return self._freq_deviation

    @property
    def pulse_shape(self):
        """The normalized pulse shape"""
        return self._pulse

    def reset(self):
        """
        Reset internal state variables
        """
        self._phase_state = 0.0
        self._zinit = np.zeros(len(self._pulse) - 1, dtype='float')

    def mod(self,myx):
        """
        CPM modulation

        v = CPMMod.mod(x) modulates the input message signal x and returns the
        modulated complex envelope in v. The message signal x must have values
        in the range [+/-1, +/-3, ..., +/-(M-1)], where M
        is the alphabet size.

        Parameters
        -----------
        x : ndarray of integers
                Message sequence to modulate, values must be odd integers on the interval
                [-(M-1), (M-1)]
                
        Returns
        -------
        v : ndarray of complex floats
                Complex modulated signal 

        """

        # Input error checking
        assert_ndarray(myx)
        assert_one_dimension(myx)
        if any(~np.isreal(myx)) == True:
            raise TypeError("input must be real")
        if (max(myx) >= self._Mary):
            raise ValueError("input must be less than M") 
        if (min(myx) <= -self._Mary):
            raise ValueError("input must be greater than -M") 
        #if not all(vt.isodd(myx)):
        #    raise ValueError("input must be an odd integer")

        # Upsample symbols
        symup = upsample(myx, self._fsT)
        
        # Filter symbols
        vf, self._zinit = lfilter(self._pulse, 1, symup, zi=self._zinit)

        # Frequency modulation
        # The integration history for cumsum(...) is maintained as part
        # of the phase_state variable
        phase0 = self._phase_state
        int_x = np.cumsum(vf)
        phase = 2.0 * np.pi * self._mod_index * int_x + phase0

        # Update the phase state
        self._phase_state = phase[-1]

        vo = np.exp(1j * phase) 

        return vo
