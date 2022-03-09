import unittest
import dp

class TestDP(unittest.TestCase):
    def test_num_score_combs(self):
        self.assertEqual(dp.num_score_combs(6, [2, 3, 4]), 3)
