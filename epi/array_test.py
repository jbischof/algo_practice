import unittest
import array
import numpy as np

class TestArray(unittest.TestCase):

	def testSortEvenOdd(self):
		self.assertEqual(array.sort_even_odd([1, 2, 3, 4]), [4, 2, 3, 1])
		self.assertEqual(array.sort_even_odd([1, 2]), [2, 1])
		self.assertEqual(array.sort_even_odd([1]), [1])
		self.assertEqual(array.sort_even_odd([]), [])

	def testFlagSort(self):
		sortArray3 = [1, 0, 2, 1, 1, 0, 2]
		array.sort_pivot(sortArray3, 0)
		self.assertEqual(sortArray3, [0, 0, 1, 1, 1, 2, 2])
		sortArray4 = [1, 0, 2, 3, 1, 3, 2, 0]
		array.four_int_sort(sortArray4)
		self.assertEqual(sortArray4, [0, 0, 1, 1, 2, 2, 3, 3])

	def testIncrementDecimal(self):
		self.assertEqual(array.increment_pos_decimal([1, 2, 9]), [1, 3, 0])
		self.assertEqual(array.increment_pos_decimal([1, 9, 9]), [2, 0, 0])
		self.assertEqual(array.increment_pos_decimal([9, 9, 9]), [1, 0, 0, 0])
		self.assertEqual(array.increment_pos_decimal([0]), [1])

	def testShiftArray(self):
		a = [1, 1, 2, 3, 4]
		array.shift_array(a, 1)
		self.assertEqual(a, [1, 2, 3, 4, 0])
		a = [1, 2, 2, 3, 4]
		array.shift_array(a, 2)
		self.assertEqual(a, [1, 2, 3, 4, 0])
		a = [1, 2, 2, 2, 2, 3, 4]
		array.shift_array_k(a, 4, 3)
		self.assertEqual(a, [1, 2, 3, 4, 0, 0, 0])
		a = [1, 1, 2, 3, 3, 3, 4, 5, 5]
		self.assertEqual(array.remove_dups_n2(a), 5)
		self.assertEqual(a, [1, 2, 3, 4, 5, 0, 0, 0, 0])
		# Getting the last one tricky
		a = [1, 2, 3, 4, 5, 5, 5]
		self.assertEqual(array.remove_dups_n2(a), 5)
		self.assertEqual(a, [1, 2, 3, 4, 5, 0, 0])
		a = [1, 1, 2, 3, 3, 3, 4, 5, 5]
		self.assertEqual(array.remove_dups(a), 5)
		self.assertEqual(a[0:5], [1, 2, 3, 4, 5])
		# Getting the last one tricky
		a = [1, 2, 3, 4, 5, 5, 5]
		self.assertEqual(array.remove_dups(a), 5)
		self.assertEqual(a[0:5], [1, 2, 3, 4, 5])

	def testPrimes(self):
		self.assertEqual(array.enum_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

	#def testPerm(self):
		#a = [0, 1, 2, 3]
		#array.perm_array(a, [3, 0, 1, 2])
		#self.assertEqual(a, [1, 2, 3, 0])
		# Two cycles
		#a = [0, 1, 2, 3]
		#array.perm_array(a, [1, 0, 3, 2])
		#self.assertEqual(a, [1, 0, 3, 2])		

	def roundNestedListFloats(self, a, k):
		""" Rounds floats in a nested list of float to the kth decimal """
		return [[round(x, k) for x in y] for y in a]

	def testMultiSample(self):
		probs = [0.1, 0.2, 0.5, 0.2]
		buckets = self.roundNestedListFloats(array.cum_prob_buckets(probs), 4)
		self.assertEqual(buckets, [[0, 0.1], [0.1, 0.3], [0.3, 0.8], [0.8, 1]])

	def testSpiralArray(self):
		a = np.array([[]])
		self.assertEqual(array.spiral_array(a), [])
		a = np.array([[1]])
		self.assertEqual(array.spiral_array(a), [1])
		a = np.array([[1, 2], [3, 4]])
		self.assertEqual(array.spiral_array(a), [1, 2, 4, 3])
		a = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
		self.assertEqual(array.spiral_array(a),
			[1, 2, 3, 6, 9, 8, 7, 4, 5])
		a = np.array([
			[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
		self.assertEqual(array.spiral_array(a),
			[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

	def testRotate90Array(self):
		a = np.array([[]])
		array.rotate90_array(a)
		self.assertEqual(a.tolist(), np.array([[]]).tolist())
		a = np.array([[1]])
		array.rotate90_array(a)
		self.assertEqual(a.tolist(), [[1]])
		a = np.array([[1, 2], [3, 4]])
		array.rotate90_array(a)
		self.assertEqual(a.tolist(), [[3, 1], [4, 2]])
		a = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
		array.rotate90_array(a)
		self.assertEqual(a.tolist(), [[7, 4, 1], [8, 5, 2],[9, 6, 3]])
		a = np.array([
			[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
		array.rotate90_array(a)
		self.assertEqual(a.tolist(),
			[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])