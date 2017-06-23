# Tests for sorting functions
import unittest
import sort

class TestSort(unittest.TestCase):

	def test_vec(self):
		return [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

	def testBubble(self):
		test_vec = self.test_vec()
		sort.bubblesort(test_vec)
		self.assertEqual(test_vec, sorted(self.test_vec()))

	def testMergeArr(self):
		self.assertEqual(sort.mergearr([1, 4], [3, 7]), [1, 3, 4, 7])
		self.assertEqual(sort.mergearr([1, 4], [3]), [1, 3, 4])
		self.assertEqual(sort.mergearr([4], [3]), [3, 4])
		self.assertEqual(sort.mergearr([1, 4], []), [1, 4])

	def testMerge(self):
		self.assertEqual(sort.mergesort(self.test_vec()), sorted(self.test_vec()))

	def testSwap(self):
		test_vec_orig = [1, 2, 3, 4]
		# Check that normal swap correct
		test_vec = test_vec_orig[:]
		sort.swap_pivot(test_vec, 3, 0)
		self.assertEqual(test_vec, [3, 2, 4, 1])
		# Check that swap correct when pivot and swap consecutive
		test_vec = test_vec_orig[:]
		sort.swap_pivot(test_vec, 2, 1)
		self.assertEqual(test_vec, [1, 3, 2, 4])
		# Check swap fails for bad indicies
		self.assertFalse(sort.swap_pivot(test_vec, 0, 3))

	def testQuick(self):
		test_vec = self.test_vec()
		sort.quicksort(test_vec, 0, len(test_vec) - 1)
		self.assertEqual(test_vec, sorted(self.test_vec()))


if __name__ == '__main__':
		unittest.main()