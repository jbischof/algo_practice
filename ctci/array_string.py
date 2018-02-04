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


def isEditDistOne(s1, s2):
  """Check if two strings have edit distance of one.
  
  Time complexity: O(N)
  Space complexity: O(1)
  """

  diff = abs(len(s1) - len(s2))
  if diff > 1:
    return False
  # Make s1 shorter string
  if len(s1) > len(s2):
    s1, s2 = s2, s1
  short_length = len(s1)

  # Whether this is the first difference between the strings or not
  first_offense = True

  if diff == 0:
    # If lengths are equal, only substitution possible
    for i in xrange(short_length):
      if s1[i] != s2[i]:
        if first_offense:
          first_offense = False
        else:
          return False
  else:
    # If lengths off by one, check for addition/deletion
    s1_pos, s2_pos = 0, 0
    for i in xrange(short_length):
      if s1[s1_pos] != s2[s2_pos]:
        if first_offense:
          first_offense = False
          s2_pos += 1
          continue
        else:
          return False
      else:
        s1_pos += 1
        s2_pos += 1

  return True


def maybeCompressString(s):
  """Compress alpha string into `char,count` form if smaller than original.

  For example, `mmmmmnnb` -> `m5n2b1`

  Time complexity: O(N)
  Space complexity: O(1)
  """

  # TODO(bischof): extend to multi-digit counts

  # First pass to determine length of compressed string
  orig_len = len(s)
  if orig_len == 0:
    return s
  prev_char = s[0]
  char_runs = 1
  for i in xrange(1, orig_len):
    if s[i] != prev_char:
      char_runs += 1
      prev_char = s[i]

  # Return original string if cannot be compressed
  new_len = char_runs * 2 
  if new_len >= orig_len:
    return s

  # Construct new string
  ret = bytearray(' ' * new_len)
  ret_pos = 0
  run_size = 1
  for i in xrange(1, orig_len + 1):
    if i < orig_len and s[i] == s[i-1]:
      run_size += 1
    else:
      ret[ret_pos : (ret_pos + 2)] = '%s%d' % (s[i-1], run_size)
      ret_pos += 2
      run_size = 1

  return str(ret)


def rotateMatrix(a):
  """Rotate an NxN array by 90 degrees right."""

  dim = len(a)
  if len(a[0]) != dim:
    raise ValueError('Array must be square.')

  size = dim
  offset = 0
  while size > 1:
    for k in xrange(size - 1): 
      i, j = offset, offset + k
      #print ((i, j), (~j, i), (~i, ~j), (j, ~i))
      a[i][j], a[~j][i], a[~i][~j], a[j][~i] = (
           a[~j][i], a[~i][~j], a[j][~i], a[i][j])
    size -= 2
    offset += 1


def isRotationPos(s1, s2, pos):
  """Check if two strings are rotations are each other from a position.

  Time complexity: O(N)
  Space complexity: O(1)
  
  Args:
    pos: position to start reading s2
  """

  if not len(s1) == len(s2):
    return False

  s1_pos, s2_pos = 0, pos
  while s1_pos < len(s1):
    if s1[s1_pos] != s2[s2_pos]:
      return False
    s1_pos += 1
    s2_pos = (s2_pos + 1) % len(s1)
  return True
    
  
def isRotationBS(s1, s2):
  """Check if two strings are rotations are each other.
  
  This implementation uses binary search. It does not actually work with current
  move left/move right rules.
  
  Time complexity: O(NlogN)
  Space complexity: O(N) (could be O(1), but need to slice for substring check.)
  """

  if not len(s1) == len(s2):
    return False

  left, right = 0, len(s1) - 1
  counter = 0
  while left < right and counter < 10:
    pos = (left + right) / 2
    print left, right, pos
    print 's1: ', s1
    print 's2: ', s2, s2[pos:]
    # Check if s2 is substring starting from pos
    if s1.find(s2[pos:]) >= 0:
      print 'substr found'
      # If true, check if full match
      if isRotationPos(s1, s2, pos):
        print 'is rotation!'
        return True
      # Otherwise need to move left
      print 'move left'
      right = pos - 1
    else:
      # Need to move right; still have tail end of s1 from pos
      print 'move right'
      left = pos + 1
    counter +=1
  return False

def isRotation(s1, s2):
  """Check if two strings are rotations are each other.
  
  This implementation uses binary search.
  
  Time complexity: O(N)
  Space complexity: O(N)
  """

  return (s2 + s2).find(s1) > 0
