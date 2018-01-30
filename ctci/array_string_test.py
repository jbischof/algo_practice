import array_string as astr
import unittest

class testArrayString(unittest.TestCase):
  
  def testisUnique(self):
    s1 = 'bobby'
    s2 = 'thelazyfox'
    self.assertFalse(astr.isUnique(s1))
    self.assertTrue(astr.isUnique(s2))
    self.assertFalse(astr.isUniqueBA(s1))
    self.assertTrue(astr.isUniqueBA(s2))

  def testCheckPermutation(self):
    s1 = 'abcd'
    s2 = 'bcda'
    s3 = 'bcfa'
    self.assertTrue(astr.checkPermutation(s1, s2))
    self.assertFalse(astr.checkPermutation(s1, s3))

  def testReplaceSpaces(self):
    s1 = bytearray('holy cow! ')
    s2 = bytearray('nospaceshere')
    astr.replaceSpaces(s1)
    astr.replaceSpaces(s2)
    self.assertEqual(s1, bytearray('holy%20cow!%20'))
    self.assertEqual(s2, bytearray('nospaceshere'))
    
