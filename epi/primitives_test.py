import unittest
import primitives

class TestPrimitives(unittest.TestCase):
	def testPropRightmost(self):
		self.assertEqual(primitives.propagate_right(0b10100), 0b10111)
		self.assertEqual(primitives.propagate_right(0b1), 0b1)
		self.assertEqual(primitives.propagate_right(0b0), 0b0)

	def testMod2(self):
		self.assertEqual(primitives.mod2(0b10111), 1)
		self.assertEqual(primitives.mod2(0b10110), 0)
		self.assertEqual(primitives.mod2(0b1), 1)
		self.assertEqual(primitives.mod2(0b0), 0)

	def testMod2(self):
		self.assertEqual(primitives.mod2(0b10111), 1)
		self.assertEqual(primitives.mod2(0b10110), 0)
		self.assertEqual(primitives.mod2(0b1), 1)
		self.assertEqual(primitives.mod2(0b0), 0)

	def testSwapBits(self):
		self.assertEqual(primitives.swap_bits(0b10111, 0, 3), 0b11110)
		self.assertEqual(primitives.swap_bits(0b10111, 0, 2), 0b10111)
		self.assertEqual(primitives.swap_bits(0b1, 0, 0), 0b1)
		self.assertEqual(primitives.swap_bits(0b0, 0, 0), 0b0)

	def testPower(self):
		self.assertEqual(primitives.power(2, 3), 8)
		self.assertEqual(primitives.power(2, 4), 16)
		self.assertEqual(primitives.power(2, 0), 1)
		self.assertEqual(primitives.power(2, 1), 2)
		self.assertEqual(primitives.power(-2, 3), -8)
		self.assertEqual(primitives.power(-2, 4), 16)
		self.assertEqual(primitives.power(-2, 0), 1)
		self.assertEqual(primitives.power(-2, 1), -2)
		self.assertEqual(primitives.power(2, -3), 1 / float(8))
		self.assertEqual(primitives.power(2, -4), 1 / float(16))
		self.assertEqual(primitives.power(2, -1), 1 / float(2))
		self.assertEqual(primitives.power(-2, -3), -1 / float(8))
		self.assertEqual(primitives.power(-2, -4), 1 / float(16))
		self.assertEqual(primitives.power(-2, -1), -1 / float(2))
		self.assertEqual(primitives.power(0, 1), 0)
		self.assertRaises(ValueError, primitives.power, 0, 0)

	def testRevInt(self):
		self.assertEqual(primitives.rev_int(1234), 4321)
		self.assertEqual(primitives.rev_int(12345), 54321)
		self.assertEqual(primitives.rev_int(1), 1)
		self.assertEqual(primitives.rev_int(-1234), -4321)
		self.assertEqual(primitives.rev_int(-12345), -54321)
		self.assertEqual(primitives.rev_int(-1), -1)

	def testRecIntersect(self):
		rec = primitives.Rectangle(primitives.Point(0, 0), 3, 4)
		# Check point interior detection
		self.assertTrue(rec.IsInterior(primitives.Point(1, -1)))
		self.assertTrue(rec.IsInterior(primitives.Point(0, 0)))
		self.assertFalse(rec.IsInterior(primitives.Point(-1, -1)))
		# Intersection
		self.assertTrue(
			primitives.RecIntersect(
				rec,
				primitives.Rectangle(primitives.Point(1, -1), 10, 10)))
		# Intersection and completely contained
		self.assertTrue(
			primitives.RecIntersect(
				rec,
				primitives.Rectangle(primitives.Point(1, -1), 1, 1)))
		# Intersect on boundary
		self.assertTrue(
			primitives.RecIntersect(
				rec,
				primitives.Rectangle(primitives.Point(-1, -1), 1, 1)))
		# No where close
		self.assertFalse(
			primitives.RecIntersect(
				rec,
				primitives.Rectangle(primitives.Point(-10, -10), 1, 1)))
