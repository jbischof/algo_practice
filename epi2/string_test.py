import unittest
import string

class TestString(unittest.TestCase):
  def testString2Int(self):
    self.assertEqual(1234, string.str2int('1234'))
    self.assertEqual('1234', string.int2str(1234))
    self.assertEqual('-1234', string.int2str(-1234))

  def testReverseSubstr(self):
    b = bytearray('bobby is great')
    string.reverse_substr(b, 0, 4)
    self.assertEqual(b, 'ybbob is great')
    b = bytearray('bobby is great')
    string.reverse_substr(b, 6, 7)
    self.assertEqual(b, 'bobby si great')
    b = bytearray('bobby is great')
    string.reverse_substr(b, 9, 13)
    self.assertEqual(b, 'bobby is taerg')

  def testReverseSentence(self):
    b = bytearray('bobby is great')
    string.reverse_sentence(b)
    self.assertEqual(b, 'great is bobby')

  def testPhoneMnemonics(self):
    self.assertEqual(string.phone_mnemonics('23'),
                     ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
    self.assertEqual(string.phone_mnemonics('203'),
                     ['a0d', 'a0e', 'a0f', 'b0d', 'b0e', 'b0f', 'c0d', 'c0e', 
                      'c0f'])
    self.assertEqual(string.phone_mnemonics2('23'),
                     ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
    self.assertEqual(string.phone_mnemonics2('203'),
                     ['a0d', 'a0e', 'a0f', 'b0d', 'b0e', 'b0f', 'c0d', 'c0e', 
                      'c0f'])
