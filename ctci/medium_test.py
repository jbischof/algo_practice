"""Tests for medium difficulty problems."""

import unittest
import medium as m


class TestMedium(unittest.TestCase):
  def testFindMinDistance(self):
    a1 = [1, 2, 11, 15]
    a2 = [4, 12, 19, 23, 127, 235]
    self.assertEqual(m.find_min_distance(a1, a2), 1)

  def testMaxPopulationYear(self):
    persons = [
        m.Person(12, 15),
        m.Person(20, 90),
        m.Person(10, 98),
        m.Person(01, 72),
        m.Person(10, 98),
        m.Person(23, 82),
        m.Person(13, 98),
        m.Person(90, 98),
        m.Person(83, 99),
        m.Person(75, 94)
    ]
    self.assertEqual(m.max_population_year(persons), 90)

  def testSubsortIndices(self):
    # Normal array
    self.assertEqual(
        m.subsort_indices([1, 2, 4, 7, 10, 11, 7, 12, 6, 6, 7, 18, 19]),
        (3, 10))
    # Already sorted array
    self.assertEqual(
        m.subsort_indices([1, 2, 4, 7, 10, 11, 12, 18, 19]), None)
    # Array with one unique item
    self.assertEqual(m.subsort_indices([1] * 10), None)
    # Concatentation of two sorted arrays
    self.assertEqual(
        m.subsort_indices([1, 2, 4, 7, 10, 11, 12, 6, 7, 10, 18, 19]),
        (3, 9))
    
