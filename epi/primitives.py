""" Bit-flipping magic. """
import math
import random

def propagate_right_slow(x):
	""" Set all zero bits after last one bit to one.
	E.g., 0b10100 -> 0b10111
	Algorithm must run in O(1) time
	Brute force method: use bitmasks to figure out first flipped bit. (Not O(1))
  Better method: using x & ~(x-1) to extract lowest set bit
	"""
	low_pos = x & ~(x - 1)
	while low_pos:
		x |= low_pos
		low_pos >>= 1
	return x

def propagate_right(x):
	""" Set all zero bits after last one bit to one.
	E.g., 0b10100 -> 0b10111
	Algorithm must run in O(1) time
	"""
	if x:
		return x | (x - 1)
	return x

def propagate_right2(x):
	""" Set all zero bits after last one bit to one.
	E.g., 0b10100 -> 0b10111
	Algorithm must run in O(1) time
	"""
	low_pos = x & ~(x - 1)
	if low_pos:
		return x | (low_pos - 1)
	return x

def mod2(x):
	""" Computes x % 2. Must run in O(1) time """
	return x & 1

def testEven(x):
	return mod2(x) == 0

def swap_bits(x, i, j):
	""" Swap bits i and j in integer x. Must run in O(1) time 
	Args:
	  x: integer
	  i, j: 0-based index, starting from right
	Returns: integer with swapped bits
	"""
	# Extract bits i and j
	mask_i = 1 << i
	bit_i = (x & mask_i) >> i
	mask_j = 1 << j 
	bit_j = (x & mask_j) >> j
	# Swap bits
	if bit_i != bit_j:
		x ^= mask_i | mask_j
	return x

def power(x, a):
	""" Calculates x to the power of a 
	Args:
	  x: double
	  a: integer
	"""
	if a == 0 and x == 0:
		raise ValueError('Cannot raise 0 to the 0 power')
	if a == 0:
		return 1
	if x == 0:
		return 0
	neg_pow = a < 0
	a = abs(a)
	half_pow = a / 2
	odd_pow = a % 2 > 0
	half_pow_value = power(x, half_pow)
	res = half_pow_value * half_pow_value
	if odd_pow:
		res *= x
	if neg_pow:
		res = 1 / float(res)
	return res

def rev_int(x):
	""" Reverse the digits of an integer """
	sint = list(str(abs(x)))
	l = len(sint)
	odd_len = l % 2 > 0
	half_len = l / 2
	reflect_pos = l - 1
	# Swap positions
	for i in range(half_len):
		sint[i], sint[reflect_pos] = sint[reflect_pos], sint[i]
		reflect_pos -= 1
	res = int("".join(sint))
	if x < 0:
		return res * -1
	return res

# def palindrome_int(x):
# 	""" Check if decimal representation of int a palindrome """
# 	# Most significant digit
# 	pow10 = math.floor(math.log(x, 10)) + 1
# 	half_pow = pow10 / 2
# 	reflect_pos = pow10
# 	for i in range(half_pow):
# 		if not x / pow(i, 10)

def fair_coin():
	if random.random() < 0.5:
		return 0
	return 1

def random_int(x):
	""" Generates a random int from 0 to (x-1) using only a fair coin. """
	# Minimal binary representation
	pow2 = int(math.floor(math.log(x, 2))) + 1
	res = x + 1
	while res >= x:
		res = 0
		for i in range(pow2):
			if fair_coin():
				res |= (1 << i)
	return res

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Rectangle():
	def __init__(self, ul, width, height):
		self.ul = ul
		self.ur = Point(self.ul.x + width, self.ul.y)
		self.ll = Point(self.ul.x, self.ul.y - height)
		self.lr = Point(self.ul.x + width, self.ul.y - height)

	def IsInterior(self, p):
		""" Check if a point is in the interior of the rectangle """
		inside_x = p.x >= self.ul.x and p.x <= self.ur.x
		inside_y = p.y >= self.ll.y and p.y <= self.ul.y
		return inside_x and inside_y

	def RecPointsInterior(self, rec):
		""" Check if any of a rectangle's point are in the interior """
		return (self.IsInterior(rec.ul) or self.IsInterior(rec.ur) or 
			self.IsInterior(rec.ll) or self.IsInterior(rec.lr))

def RecIntersect(rec1, rec2):
	""" Check if any intersection between two rectangles """
	return rec1.RecPointsInterior(rec2) or rec2.RecPointsInterior(rec1)

	""" Actually just need to check overlap of x and y range """

