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

    def test_nextpower2(self):
        x = 514
        y = vt.nextpower2(x)
        yCorrect = 10
        self.assertEqual(y,yCorrect)

def mysuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSigProcFunctions)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
