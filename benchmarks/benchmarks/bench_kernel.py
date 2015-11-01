
import numpy as np
import velvet as vt
import scipy.signal

convolve = scipy.signal.convolve

class Kernel(object):
    """
    An example benchmark that times the performance of various DSP 
    kernel operations.
    """
    params = [10, 100, 1000]

    def setup(self, n):
        self.x = np.random.randn(n)
        self.h = np.random.randn(n)

    def time_conv(self, n):
        vt.conv(self.x, self.h)

    time_conv.param_names = ['N']
