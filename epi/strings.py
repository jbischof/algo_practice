import math
import string

HEX_DIGITS = '0123456789ABCDEFG'

def string2int(x):
	""" Convert a string representation of an int to int """
	res = 0
	neg = False
	if x[0] == '-':
		neg = True
		x = x[1: ]
	L = len(x)
	for i in range(L):
		res += (ord(x[i]) - 48) * pow(10, i)
	if neg:
		res *= -1
	return res

def int2string(x, base=10):
	""" Convert integer to string
	Args:
		x: int in base 10
		base: base of output string <= 16 """
	if x == 0:
		return '0'
	res = []
	if x < 0:
		res.append('-')
		x = abs(x)
	power = int(math.floor(math.log(x, base))) + 1
	for i in reversed(range(power)):
		res.append(HEX_DIGITS[x // base**i])
		x = x % base**i
	return ''.join(res)

def convertBase(s, b1, b2):
	""" Convert integer in one base to another 
	Args:
		s: string representing positive integer, using vals (0-F)
		b1, b2: base and desired base of integer (vals 2-16)
	Returns: string representing integer in desired base """
	int10 = 0
	res = ''
	# First get integer in base 10
	for i, val in enumerate(s[::-1]):
		int10 += int(val, b1) * b1**i
	# Convert base10 to desired base b2
	return int2string(int10, base=b2)

def remove_item(a, c):
	""" Remove all instances of char 'c' from array
	Args:
		a: input array
		c: character to be removed
	Returns:
		length of pruned array
	"""
	# Last index of final array
	index = 0
	for val in a:
		if val != c:
			a[index] = val
			index += 1
	return index

def replace_item(a, c, r, maxlen=None):
	""" Replace all occurrences of s1 with s2 in input string
	Args:
		a: input array
		c: character to be replaced
		r: replacement array
		maxlen: Maximum length of interest for amended string (>= 1)
	"""
	orig_L = len(a)
	r = r[::-1]
	r_L = len(r)
	# Extend array by the number of chars to be added
	for val in a:
		if val == c:
			for j in range(r_L - 1):
				a.append(0)
	new_L = len(a)
	# Write new values in array from back
	write_index = new_L - 1
	for i in reversed(range(orig_L)):
		if a[i] == c:
			for val in r:
				a[write_index] = val
				write_index -= 1
		else:
				a[write_index] = a[i]
				write_index -= 1

def is_palindrome(s):
	""" Detects if string is a palindrome, omitting non-alphanumeric characters
	Args:
		s: string
	Returns:
		Boolean indicating if string is a palindrome
	"""
	front_idx, back_idx = 0, len(s) - 1
	while front_idx < back_idx:
		while not s[front_idx].isalnum() and front_idx < back_idx:
			front_idx += 1
		while not s[back_idx].isalnum() and front_idx < back_idx:
			back_idx -= 1
		if not s[front_idx].lower() == s[back_idx].lower():
			return False
		front_idx += 1
		back_idx -= 1
	return True

def reverse_word(b, i0, i1):
	""" Reverse a word in a sentence
	Args:
		b: A byte array
		i0, i1: Index of first, last position of word in sentence.
	"""
	while i0 < i1:
		b[i0], b[i1] = b[i1], b[i0]
		i0 += 1
		i1 -= 1

def byte_isalpha(x):
	""" Determine if a byte represents an alpha character """
	return chr(x).isalpha()

def reverse_sentence(b):
	""" Reverse the order of words in a sentence.
	Args:
		b: A byte array containing only alpha chars and whitespace.
	Returns:
		None. An in-place operation.
	"""
	# Reverse string
	b.reverse()
	# Iterate through string and delimit words with whitespace
	i0, i1 = 0, 0
	for i in range(1, len(b)):
		b_im1, b_i = byte_isalpha(b[i-1]), byte_isalpha(b[i])
		if b_im1 and b_i:
			# Still inside a word, continue
			i1 += 1
		elif b_im1 and not b_i:
			# At the end of a word, pass for reversal
			reverse_word(b, i0, i1)
		elif not b_im1 and b_i:
			# At the beginning of a word, reset counters
			i0, i1 = i, i
		else:
			# Otherwise in the middle of whitespace, keep moving
			continue

R2I = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def roman2int(s):
	""" Converts a string representing a Roman numerial to an int
	Args:
		s: A string with values I, V, X, L, C, D, M
	Returns:
		integer
	"""
	res = 0
	for i in range(len(s)):
		# If value of previous letter less than current, actually needed to subtract
		if i > 0 and R2I[s[i-1]] < R2I[s[i]]:
			res -= 2 * R2I[s[i-1]]
		res += R2I[s[i]]
	return res