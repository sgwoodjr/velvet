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

class TestCommFunctions(unittest.TestCase):

    def test_biterr(self):
        x = np.array([0, 1, 1, 0])
        y = np.array([1, 1, 0, 0])
        n = vt.biterr(x, y)
        self.assertEqual(n, 2)

        y = np.array([0, 1, 1, 0])
        n = vt.biterr(x, y)
        self.assertEqual(n, 0)

    def test_qfunc(self):
        x = np.array([0,1,2,3])
        y = vt.qfunc(x)
        yCorrect = np.array([ 0.5,0.15865525,0.02275013,0.0013499 ])
        for ind in np.arange(len(y)):
            self.assertAlmostEqual(y[ind],yCorrect[ind])

def mysuite():
        return unittest.TestLoader().loadTestsFromTestCase(TestCommFunctions)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
    

