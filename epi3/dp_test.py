import unittest
import dp

class TestDP(unittest.TestCase):
    def test_fib_bu(self):
        self.assertEqual(dp.fib_bu(0), 0)
        self.assertEqual(dp.fib_bu(1), 1)
        self.assertEqual(dp.fib_bu(2), 1)
        self.assertEqual(dp.fib_bu(9), 34)
        self.assertEqual(dp.fib_bu(15), 610)

    def test_num_score_combs(self):
        self.assertEqual(dp.num_score_combs(6, [2, 3, 4]), 3)

    def test_longest_nd_subsequence(self):
        a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
        self.assertEqual(dp.longest_nd_subsequence(a), 4)
