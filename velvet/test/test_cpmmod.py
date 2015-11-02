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

class TestCPM(unittest.TestCase):

    def test_mod(self):
        cpm = vt.CPMMod(2, 1.0/2400, 0.5, np.ones(4), 4)
        syms = np.random.randint(0, 2, 1000)
        v = cpm.mod(2*syms-1)

        # Simple demod
        temp = np.arctan2(np.imag(v), np.real(v))
        temp = np.diff(temp)
        yCorrect = np.clip(temp[0::4] > 0, 0, 1)
        for ind in np.arange(len(yCorrect)):
            self.assertAlmostEqual(syms[ind],yCorrect[ind])

    def test_reset(self):
        cpm = vt.CPMMod(4, 1.0/2400, 0.5, np.ones(4), 4)
        syms = np.random.randint(0,4,30)
        y1 = cpm.mod(2*syms - (4-1))
        cpm.reset()
        y2 = cpm.mod(2*syms - (4-1))
        for ind in np.arange(len(y1)):
            self.assertAlmostEqual(y1[ind],y2[ind])

    def test_mod_state(self):
        cpm = vt.CPMMod(4, 1.0/2400, 0.75, np.ones(4), 4)
        syms = np.random.randint(0,4,100)
        y1 = cpm.mod(2*syms - (4-1))
        cpm.reset()
        temp1 = cpm.mod(2*syms[0:50] - (4-1))
        temp2 = cpm.mod(2*syms[50:] - (4-1))
        y2 = np.concatenate((temp1,temp2))
        for ind in np.arange(len(syms)):
            self.assertAlmostEqual(y1[ind],y2[ind])

def mysuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCPM)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
