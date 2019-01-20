"""Adventures in bit flipping. This will totally come up!"""
import random

def parity(x):
  """Determines whether number of set bits in word are odd.

  Time complexity: O(n), where n is width of integer.

  Args:
    x: integer
  
  Returns:
    True if parity is one, False otherwise
  """

  res = 0
  while x:
    # XOR flips last bit
    res ^= 1
    # x & (x - 1) removes lowest set bit
    x &= x - 1
  return bool(res)


def parity64(x):
  """Compute parity faster using XOR, assuming x is has up to 64 bits.

  Time complexity: O(log n), where n is width of integer, but in reality O(1)
                   for any given program definition (parityXX).

  Args:
    x: integer
  
  Returns:
    True if parity is one, False otherwise
  """

  x ^= x >> 32
  x ^= x >> 16
  x ^= x >> 8
  x ^= x >> 4
  x ^= x >> 2
  x ^= x >> 1
  return bool(x & 1)


def swap_bits(x, i, j):
  """Swap two bits in int.

  Args:
    x: integer
    i, j: Bit positions 0-63 to swap
  
  Returns:
   Int with swapped bits. 
  """

  # Check if bits are equal
  if (x >> i) & 1 != (x >> j) & 1:
    # Flip both if not
    x ^= (1 << i) | (1 << j)

  return x


def power(x, y):
  """Raise float x to the power y, a positive int.
  
  Idea that x^(0b101) = 1 * x^2^0 + 0 * x^2^1 + 1 * x^2^2, so keep squaring
  x and dividing y by 2. If y % 2 = 1, multiply in the latest x.

  Time complexity: O(log n), where n is the width of y
  """

  res = 1
  while y:
    if y & 1:
      res *= x
    x *= x
    y >>= 1
  return res


def rev_int(x):
  """Reverse base-10 representation of int."""

  res, remain = 0, abs(x)
  while remain:
    res = res * 10 + remain % 10
    remain //= 10
  return res if x > 0 else -res


def coin():
  return int(random.getrandbits(1))


def rand_int(n):
  """Generates random int from 0 to n."""

  while True:
    res, power, remain = 0, 0, n
    while remain:
      res |= coin() << power
      power += 1
      remain >>= 1
    if res <= n:
      return res
