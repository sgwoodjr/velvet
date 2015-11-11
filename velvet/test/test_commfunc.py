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

    def test_berawgn_cpfsk(self):
        EbNodB = np.arange(10)
        ber = vt.berawgn(EbNodB,'cpfsk', 2, 0.5, 1)
        berC = np.array([  7.86496035e-02,   5.62819520e-02,   3.75061284e-02,
            2.28784076e-02,   1.25008180e-02,   5.95386715e-03,
            2.38829078e-03,   7.72674815e-04,   1.90907774e-04,
            3.36272284e-05])
        for ind in np.arange(len(ber)):
            self.assertAlmostEqual(ber[ind],berC[ind])

    def test_berawgn_cpfsk_ValueError(self):
        EbNodB = np.arange(10)
        self.assertRaises(ValueError, vt.berawgn, EbNodB, 'cpfsk', 2)

    def test_berawgn_modtype_ValueError(self):
        EbNodB = np.arange(10)
        unsupported_mod_type = 'qam'
        self.assertRaises(ValueError, vt.berawgn, EbNodB, unsupported_mod_type, 2)

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
    

