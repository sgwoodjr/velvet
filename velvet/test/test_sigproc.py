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

class TestSigProcFunctions(unittest.TestCase):

    def test_conv(self):
        x = np.array([1,2,3])
        h = np.array([0,1,0.5])
        y = vt.conv(x,h)
        yCorrect = np.array([  7.49400542e-16,   1.00000000e+00,   2.50000000e+00,
            4.00000000e+00,   1.50000000e+00])

        for ind in np.arange(len(y)):
            self.assertAlmostEqual(y[ind],yCorrect[ind])

    def test_conv_complex(self):
        x = np.array([1,2,3])
        h = np.array([0,1,0.5])
        y = vt.conv(x,h*1j)
        yCorrect = np.array([-4.99600361e-16 +7.77156117e-16j,
            2.22044605e-16 +1.00000000e+00j,
            6.60257881e-17 +2.50000000e+00j,
            -3.88578059e-16 +4.00000000e+00j,   1.72084569e-15 +1.50000000e+00j])
            
        for ind in np.arange(len(y)):
            self.assertAlmostEqual(y[ind],yCorrect[ind])

    def test_nextpower2(self):
        x = 514
        y = vt.nextpower2(x)
        yCorrect = 10
        self.assertEqual(y,yCorrect)

    def test_upsample(self):
        x = np.array([1, 2, 3])
        y = vt.upsample(x, 2)

        yCorrect = np.array([1, 0, 2, 0, 3, 0])

        for ind in np.arange(len(y)):
            self.assertAlmostEqual(y[ind], yCorrect[ind])

def mysuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSigProcFunctions)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
