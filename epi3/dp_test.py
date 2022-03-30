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

    def test_min_weight_path_triangle(self):
        t = [
            #0
            [2], # level 0
            #0  1 
            [4, 4], # level 1
            #0  1  2
            [8, 5, 6], # level 2
            #0  1  2  3
            [4, 2, 6, 2], # level 3
            #0  1  2  3  4
            [1, 5, 2, 3, 4], # level 4
        ]
        self.assertEqual(dp.min_weight_path_triangle(t), 15)

    def test_has_array_sequence(self):
        a = [
                [1, 2, 3],
                [3, 4, 5],
                [5, 6, 7],
        ]
        self.assertTrue(dp.has_array_sequence(a, [1, 3, 4, 6]))
        self.assertFalse(dp.has_array_sequence(a, [1, 2, 3, 4]))
