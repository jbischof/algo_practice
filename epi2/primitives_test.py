import unittest
import primitives

class PrimitivesTest(unittest.TestCase):
  def testParity(self):
    # Even bits
    self.assertFalse(primitives.parity(0b10110111))
    # Odd bits
    self.assertTrue(primitives.parity(0b10110110))
    # No bits
    self.assertFalse(primitives.parity(0b0))

  def testParity64(self):
    # Even bits
    self.assertFalse(primitives.parity64(0b10110111))
    # Odd bits
    self.assertTrue(primitives.parity64(0b10110110))
    # No bits
    self.assertFalse(primitives.parity64(0b0))

  def testSwapBits(self):
    # Bits equal
    self.assertEqual(0b1010, primitives.swap_bits(0b1010, 1, 3))
    # Bits not equal
    self.assertEqual(0b1100, primitives.swap_bits(0b1010, 1, 2))
    # Bits bigger than int
    self.assertEqual(0b1010, primitives.swap_bits(0b1010, 5, 7))

  def testPower(self):
    self.assertEqual(3**1, primitives.power(3, 1))
    self.assertEqual(3**5, primitives.power(3, 5))
    self.assertEqual(3**8, primitives.power(3, 8))

  def testRevInt(self):
    self.assertEqual(1104, primitives.rev_int(4011))
    self.assertEqual(-1104, primitives.rev_int(-4011))
    
