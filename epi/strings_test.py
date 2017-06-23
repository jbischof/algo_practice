import strings
import unittest

class TestString(unittest.TestCase):
	def testString2Int(self):
		self.assertEqual(strings.string2int('0'), 0)
		self.assertEqual(strings.string2int('1'), 1)
		self.assertEqual(strings.string2int('101'), 101)
		self.assertEqual(strings.string2int('-1'), -1)
		self.assertEqual(strings.string2int('-101'), -101)	

	def testInt2String(self):
		self.assertEqual(strings.int2string(0), '0')
		self.assertEqual(strings.int2string(1), '1')
		self.assertEqual(strings.int2string(101), '101')
		self.assertEqual(strings.int2string(-1), '-1')
		self.assertEqual(strings.int2string(-101), '-101')
		self.assertEqual(strings.int2string(2575, 16), 'A0F')	

	def testConvertBase(self):
		self.assertEqual(strings.convertBase('615', 7, 13), '1A7')

	def testDeleteItem(self):
		a = ['c', 'a', 'x', 'a']
		self.assertEqual(strings.remove_item(a, 'v'), 4)
		self.assertEqual(a, ['c', 'a', 'x', 'a'])
		a = ['c', 'a', 'x', 'a']
		self.assertEqual(strings.remove_item(a, 'a'), 2)
		self.assertEqual(a[: 2], ['c', 'x'])

	def testReplaceItem(self):
		a = ['c', 'b', 'x', 'u']
		strings.replace_item(a, 'a', ['d', 'd'])
		self.assertEqual(a, ['c', 'b', 'x', 'u'])
		a = ['c', 'a', 'x', 'a']
		strings.replace_item(a, 'a', ['d', 'd'])
		self.assertEqual(a, ['c', 'd', 'd', 'x', 'd', 'd'])

	def testIsPalindrome(self):
		s = 'Madam, I\'m Adam'
		self.assertTrue(strings.is_palindrome(s)) 
		s = 'Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.'
		self.assertTrue(strings.is_palindrome(s))
		# An obscene palindrome
		s = 's?!@#a*&d^%^a&*(^s'
		self.assertTrue(strings.is_palindrome(s))
		s = 'Ma\'am, I\'m Adam'
		self.assertFalse(strings.is_palindrome(s))
		# Obscene, but not a palindrome
		s = 's?!@#a*&dx^%^a&*(^s'
		self.assertFalse(strings.is_palindrome(s))

	def testReverseWord(self):
		b = bytearray('I love PuPPies!')
		strings.reverse_word(b, 0, 0)
		self.assertEqual(b, bytearray('I love PuPPies!'))
		b = bytearray('I love PuPPies!')
		strings.reverse_word(b, 2, 5)
		self.assertEqual(b, bytearray('I evol PuPPies!'))
		b = bytearray('I love PuPPies!')
		strings.reverse_word(b, 7, 13)
		self.assertEqual(b, bytearray('I love seiPPuP!'))

	def testReverseSentence(self):
		b = bytearray('I love PuPPies!')
		strings.reverse_sentence(b)
		self.assertEqual(b, bytearray('!PuPPies love I'))

	def testRoman2Int(self):
		self.assertEqual(strings.roman2int('L'), 50) 
		self.assertEqual(strings.roman2int('XLI'), 41)
		self.assertEqual(strings.roman2int('LIV'), 54)
		self.assertEqual(strings.roman2int('LVII'), 57)
		self.assertEqual(strings.roman2int('LIX'), 59)
		self.assertEqual(strings.roman2int('MCMLIX'), 1959)
