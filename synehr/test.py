import unittest

from synehr import constrained_sum_sample_pos,syn_ehr,SizeValueError

import numpy as np

class Testsynehrpackage(unittest.TestCase):
    def test_add(self):
        res=constrained_sum_sample_pos(5,1)
        self.assertEqual(sum(res),1)
    # def test_input_synehr(self):
    #     with self.assertRaises(SizeValueError):
    #         syn_ehr(size=20)
