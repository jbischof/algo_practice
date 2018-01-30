"""Array and string problems."""

def isUnique(s):
  """Determine if string has all unique characters.
  
  Time complexity: O(N)
  Space complexity: O(N)
  """

  byte_set = set()
  for char in s:
    if char in byte_set:
      return False
    else:
      byte_set.add(char)
  return True


def isUniqueBA(s):
  """Solve unique string problem using bit-arrays.

  Can use length 256 bit-array since processing bytes.
  
  Time complexity: O(N)
  Space complexity: O(1)
  """

  a = [False] * 256
  for char in s:
    pos = ord(char)
    if a[pos]:
      return False
    else:
      a[pos] = True
  return True


def checkPermutation(s1, s2):
  """Check if two strings are permutations.

  Time complexity: O(n), where `n` is length of string
  Space: O(n)
  """

  if len(s1) != len(s2):
    return False
  arr = [0] * 256
  for char in s1:
    arr[ord(char)] += 1
  for char in s2:
    arr[ord(char)] -= 1
    if arr[ord(char)] < 0:
      return False
  return True


def replaceSpaces(b):
  """Replace spaces in bytearray with `%20` for URLs.
  
  Time complexity: O(N)
  Space complexity: O(1)
  """

  RPL = '%20'
  # Original length of string
  l = len(b)
  # Add padding to byte array
  for char in b:
    if chr(char) == ' ':
      b.extend('00')

  # Write array from back
  orig_pos, new_pos = l - 1, len(b) - 1
  while orig_pos >= 0:
    if chr(b[orig_pos]) == ' ':
      b[(new_pos - 2) : (new_pos + 1)] = RPL
      new_pos -= 3
    else:
      b[new_pos] = b[orig_pos]
      new_pos -= 1
    orig_pos -= 1

