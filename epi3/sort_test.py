import unittest
import sort

class TestSort(unittest.TestCase):
    def test_list_intersection(self):
        a = [1, 3, 5, 5, 7, 9]
        b = [2, 2, 3, 3, 5, 8]
        self.assertListEqual(sort.list_intersection(a, b), [3, 5])

    def test_merge_disjoint_intervals(self):
        # Some overlap
        a = [(-4, -1), (0, 2), (3, 6), (7, 9), (11, 12), (14, 17)]
        d = (1, 8)
        self.assertListEqual(
                sort.merge_disjoint_intervals(a, d), 
                [(-4, -1), (0, 9), (11, 12), (14, 17)]
        )
        # No overlap
        a = [(-4, -1), (0, 2), (3, 4), (7, 9), (11, 12), (14, 17)]
        d = (5, 6)
        self.assertListEqual(
                sort.merge_disjoint_intervals(a, d), 
                [(-4, -1), (0, 2), (3, 4), (5, 6), (7, 9), (11, 12), (14, 17)]
        )
        # Contained within other interval
        a = [(-4, -1), (0, 2), (3, 4), (7, 9), (11, 12), (14, 17)]
        d = (8, 9)
        self.assertListEqual(
                sort.merge_disjoint_intervals(a, d), 
                [(-4, -1), (0, 2), (3, 4), (7, 9), (11, 12), (14, 17)]
        )

    def test_max_interval_overlap(self):
        a = [(0, 3), (2, 3), (4, 10), (5, 8), (6, 9), (10, 11), (11, 12)]
        self.assertEqual(sort.max_interval_overlap(a), 3)

