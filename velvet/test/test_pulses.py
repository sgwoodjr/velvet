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

class TestPulseFunctions(unittest.TestCase):

    def test_rectpulse(self):
        u = vt.rectpulse(1, 4)
        uCorrect = np.ones(4) / 8.0

        for ind in np.arange(len(u)):
            self.assertAlmostEqual(u[ind],uCorrect[ind])


def mysuite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPulseFunctions)

if __name__ == '__main__':
    suite = mysuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
    

