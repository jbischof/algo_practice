"""Adventures in strings, the gateway to NLP!"""
import copy

def str2int(s):
  """Convert string representation of integer to int."""

  ret = 0
  mult = 1
  for i in range(len(s)):
    ret += (ord(s[~i]) - 48) * mult
    mult *= 10
  return ret


def int2str(n):
  """Convert int to string representation."""

  s = bytearray()

  neg = False
  if n < 0:
    neg = True
    n = abs(n)

  while n:
    s.append(chr(n % 10 + 48))
    n //= 10

  if neg:
    s.append('-')

  s.reverse()
  return str(s)


def reverse_substr(b, start, end):
  """Reverse chars in substring of bytearray."""

  length = end - start + 1
  for i in range(length // 2):
    b[start + i], b[end - i] = b[end - i], b[start + i]
  return


def reverse_sentence(b):
  """Reverse order of words in a sentence.

  Time complexity: O(n)
  Space complexity: O(1)

  Args:
    b: A space-delimited bytearray with a sequence of words

  Returns:
    Bytearray with order of words reversed.
  """

  b.reverse()
  start = 0
  last_char = ' '
  for i in range(len(b)):
    char = chr(b[i])
    if last_char.isspace() and char.isalpha():
      # Beginning of word
      start = i
    elif last_char.isalpha() and char.isspace():
      # End of word: reverse it!
      reverse_substr(b, start, i - 1)
    elif char.isalpha() and i == len(b) - 1:
      # End of word at end of sentence: reverse it!
      reverse_substr(b, start, i)
    last_char = char

  return


NUM2INT = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

def phone_mnemonics(s):
  """Enumerate all mnemonics pertaining to a phone number s.

  Time complexity: O(n^2 * 4^n)
  Space complexity: O(1)

  Could improve time complexity by using bytearrays, but then the answer
  wouldn't look so cool.

  Args:
    s: A string of digits

  Returns:
    List of string mnemonics
  """

  seqs = [bytearray('')]
  for num in s:
    if num in NUM2INT:
      seqs = [copy.copy(seq) + n for seq in seqs for n in NUM2INT[num]]
  return seqs


def phone_mnemonics2_helper(pos, s, partial_seq, seqs):
  """Recursive helper function for phone_mnemonics2."""

  # Base case: complete sequence
  if pos >= len(s):
    seqs.append(''.join(partial_seq))
    return

  # Recursive case: partial sequence
  for char in NUM2INT[s[pos]]:
    partial_seq[pos] = char
    phone_mnemonics2_helper(pos + 1, s, partial_seq, seqs)
  return

def phone_mnemonics2(s):
  """Recursive version of `phone_mnemonics`.

  Time complexity: O(n * 4^n)
  Space complexity: O(n)

  Args:
    s: A string of digits

  Returns:
    List of string mnemonics
  """

  seqs = []
  partial_seq = [None] * len(s)
  phone_mnemonics2_helper(0, s, partial_seq, seqs)
  return seqs
