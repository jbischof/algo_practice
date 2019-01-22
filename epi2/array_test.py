import unittest
import array

class TestArray(unittest.TestCase):
  def testTwoPart(self):
    a = [0, 3, 1, 0, 2, 1]
    self.assertEqual(array.two_part(a, value=1, start_pos=0), 4)
    self.assertEqual(a, [0, 1, 1, 0, 2, 3])
    # Non-zero `start_pos`
    a = [0, 3, 1, 0, 2, 1]
    self.assertEqual(array.two_part(a, value=1, start_pos=2), 5)
    self.assertEqual(a, [0, 3, 1, 0, 1, 2])

  def testDNF(self):
    a = [0, 3, 1, 0, 2, 1]
    array.dnf(a, pivot_pos=2)
    self.assertEqual(a, [0, 0, 1, 1, 3, 2])

  def testArrayGame(self):
    self.assertTrue(array.array_game([3, 3, 1, 0, 2, 0, 1]))
    self.assertFalse(array.array_game([3, 2, 0, 0, 2, 0, 1]))

  def testBestStockSale(self):
    self.assertEqual(array.best_stock_sale([310, 315, 275, 295, 260, 270, 290,
                                            230, 255, 250]), (4, 6))
