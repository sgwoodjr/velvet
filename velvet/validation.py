"""Developer validation functions
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
__all__ = ['assert_ndarray', 'assert_complex', 'assert_one_dimension']


def assert_ndarray(x):
    if not isinstance(x, np.ndarray):
        raise TypeError("Input must be an ndarray")

def assert_one_dimension(x):
    if x.ndim != 1:
        raise TypeError("Input must have 1-dimension")
        
def assert_complex(x):
    if np.all(np.isreal(x)):
        raise TypeError("Input must be complex")
