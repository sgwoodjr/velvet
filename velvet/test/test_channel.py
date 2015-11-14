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

    # There may be issues with the portability of the following test
    def test_awgn(self):
        x = np.arange(4) + 1j*np.arange(4)
        np.random.seed(0)
        y = vt.awgn(x, 20)
        yCorrect = np.array([ 0.33002397+0.34938811j,  1.07486256+0.81716805j,
            2.18310511+2.17774527j,  3.41923273+2.97168366j])
      
        for ind in xrange(len(y)):
            self.assertAlmostEqual(np.real(y[ind]),np.real(yCorrect[ind]))
            self.assertAlmostEqual(np.imag(y[ind]),np.imag(yCorrect[ind]))

    def test_awgn_real(self):
        x = np.arange(4)
        np.random.seed(0)
        y = vt.awgn(x,20)
        yCorrect = np.array([ 0.30554283,  1.06930926,  2.16952239,  3.38813409])
      
        for ind in xrange(len(y)):
            self.assertAlmostEqual(y[ind],yCorrect[ind])

def mysuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSigProcFunctions)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
    
