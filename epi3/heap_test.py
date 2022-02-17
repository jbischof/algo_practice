import heap
import unittest

class TestHeap(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertListEqual(
                heap.merge_sorted_arrays(
                    [1, 4, 8], [2, 3, 9], [6, 7]),
                [1, 2, 3, 4, 6, 7, 8, 9]
        )

    def test_streaming_median(self):
        a = [1, 0, 3, 5, 2, 0, 1]
        self.assertListEqual(
                heap.streaming_median(iter(a)),
                [1, 0.5, 1, 2, 2, 1.5, 1]
        )

