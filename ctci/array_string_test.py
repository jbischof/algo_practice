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

  def testIsEditDistanceOne(self):
    self.assertTrue(astr.isEditDistOne('bob', 'bomb'))
    self.assertTrue(astr.isEditDistOne('bomb', 'bob'))
    self.assertTrue(astr.isEditDistOne('bob', 'bop'))
    self.assertTrue(astr.isEditDistOne('bob', 'bo'))
    self.assertFalse(astr.isEditDistOne('bob', 'slob'))
    self.assertFalse(astr.isEditDistOne('bob', 'bebop'))

  def testMaybeCompressString(self):
    self.assertEqual(astr.maybeCompressString(''), '')
    self.assertEqual(astr.maybeCompressString('aabcccccaaa'), 'a2b1c5a3')
    self.assertEqual(astr.maybeCompressString('bobby'), 'bobby')
    
  def testRotateMatrix(self):
    a = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    a_rotate = [[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]]
    astr.rotateMatrix(a)
    self.assertEqual(a, a_rotate)

  def testIsRotationPos(self):
    self.assertTrue(astr.isRotationPos('waterbottle', 'erbottlewat', 8))
    self.assertFalse(astr.isRotationPos('waterbottle', 'erbottlewat', 3))
    self.assertFalse(astr.isRotationPos('gollum', 'column', 2))
    self.assertTrue(astr.isRotationPos('eeeweeeeewe', 'eeeweeeewee', 5))

  def testIsRotationBS(self):
    self.assertTrue(astr.isRotationBS('waterbottle', 'erbottlewat'))
    self.assertFalse(astr.isRotationBS('gollum', 'column'))
    self.assertTrue(astr.isRotationBS('eeeweeeeewe', 'eeeweeeewee'))
    # This one seems to be counterexample: from position 5 have 'eeewee' which 
    # is a match for the start of s1 so move left, but actually need to move 
    # right since correct answer is last pos.
    #self.assertTrue(astr.isRotationBS('eeeweeeeewe', 'eeweeeeewee'))
    self.assertFalse(astr.isRotationBS('eeeweeeeewe', 'eeeweeeewe'))

  def testIsRotation(self):
    self.assertTrue(astr.isRotation('waterbottle', 'erbottlewat'))
    self.assertFalse(astr.isRotation('gollum', 'column'))
    self.assertTrue(astr.isRotation('eeeweeeeewe', 'eeeweeeewee'))
    self.assertTrue(astr.isRotation('eeeweeeeewe', 'eeweeeeewee'))
    self.assertFalse(astr.isRotation('eeeweeeeewe', 'eeeweeeewe'))
