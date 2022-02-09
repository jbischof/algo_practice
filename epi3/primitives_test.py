import primitives
import unittest

class PrimitivesTest(unittest.TestCase):
    def test_count_bits(self):
        self.assertEqual(primitives.count_bits(0), 0)
        self.assertEqual(primitives.count_bits(1), 1)
        # 1000 is '0b1111101000'
        self.assertEqual(primitives.count_bits(1000), 6)

    def test_parity(self):
        self.assertEqual(primitives.parity(0), 0)
        self.assertEqual(primitives.parity(1), 1)
        self.assertEqual(primitives.parity(1000), 0)
        self.assertEqual(primitives.parity(1001), 1)

    def test_swap_bits(self):
        self.assertEqual(primitives.swap_bits(12, 1, 3), 6)

    def test_reverse_bits(self):
        # 19 is 0b10011, 25 is 0b11001
        self.assertEqual(primitives.reverse_bits(19, 5), 25)
