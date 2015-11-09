#!/usr/bin/env python

#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

import unittest
import numpy as np
import velvet as vt

class TestUtilFunctions(unittest.TestCase):

    def test_isodd(self):
        x = np.array([1,2,1,1,-3,-4,7,8,9,10,-2,1,-3,5,6,7,-10])
        y = vt.isodd(x)

        yCorrect = np.array([1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0])
        for ind in np.arange(len(y)):
            self.assertEqual(y[ind],yCorrect[ind])

    def test_scalar_int_ValueError(self):
        # Input must be an integer
        self.assertRaises(ValueError, vt.isodd, 3.4);

    def test_ndarray_int_ValueError(self):
        # Input must be an integer
        self.assertRaises(ValueError, vt.isodd, np.array([1, 1, 4.0]))


def mysuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestUtilFunctions)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
    
