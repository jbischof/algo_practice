"""String theory."""

def utfb(s):
    """Return bytearray in utf-8 from string."""

    return bytearray(s, 'utf-8')


def spreadsheet_encoding(s):
    """Map column name to column number in spreadsheet.

    Spreadsheet column ids are A-Z, AA, AB, ..., AZ, AAA, AAB,

    Idea: encoding is essentially a base 26 integer; just need to map char to 
    number.
    Time: O(N), Space: O(1)
    """

    def char2num(x):
        return ord(x) - 65 + 1

    ret = 0
    for i, char in enumerate(reversed(s)):
        ret += char2num(char)*26**i
    return ret
    

def reverse_range(s, i, j):
    """Reverse chars in a string from positions i to j (inclusive)."""

    while i < j:
        s[i], s[j] = s[j], s[i]
        i, j = i + 1, j - 1


def reverse_words(s):
    """Reverse all words (whitespace delimited) in a sentence.
    
    Given a string like "Bob likes Alice" rewrite it as "Alice likes Bob"

    Args:
        s: A bytearray

    Idea: Break string into an array of words and then just reverse that array.
    Time: O(N) to make the list, reverse it, and write it back out to a string
    Space: O(N) to write the words into the list and a new string.
    (Time and space for manipulating the words dominated by the chars.)

    Idea: If don't want to use space, can do two passes on string. First reverse
    entire string and then reverse the individual words in a second pass.
    Time: O(N)
    Space: O(1)

    Test:
    '012345678901234'
    'Bob likes Alice'
    wstart, i
    0, 3
    'boB likes Alice'
    4, 9
    'boB sekil Alice'
    10, 14
    'boB sekil ecilA'
    """
    
    s.reverse()
    wstart = 0
    WS = set([ord(" ")])
    for i, c in enumerate(s):
        if c in WS:
            # End of word
            reverse_range(s, wstart, i - 1)
            wstart = i + 1
        elif i == len(s) - 1:
            reverse_range(s, wstart, i)



def reverse_words2(s):
    """Reverse all words (whitespace delimited) in a sentence.
     This version will be robust to any whitespace pattern.
    
    Given a string like "Bob likes Alice" rewrite it as "Alice likes Bob"

    Args:
        s: A bytearray
    """

    s.reverse()
    c_prev = " "
    for i, c in enumerate(s):
        c = chr(c)
        if c_prev.isspace() and not c.isspace():
            # Start of word
            wstart = i
        elif not c_prev.isspace() and c.isspace():
            # End of word
            reverse_range(s, wstart, i - 1)
        elif not c.isspace() and i == len(s) - 1:
            # Word at the end of the string
            reverse_range(s, wstart, i)
        # Otherwise in the middle of a word or a span of ws; do nothing.
        c_prev = c


def next_look_and_say(s):
    """Return next look and say from previous state.

    Given an string integer like "11233", next item in sequence is number of
    each consecutive int and the int type, i.e., "211223" -> "12212213"

    Time: O(N) where N length of string.
    Space: O(N) to make new string. New string at most length 2N.

    Example:
    s: "21223"
    j, c, start, last_char, ret
    1, "1", 0, "2", "" -> "12"
    2, "2", 1, "1", "12" -> "1211"
    3, "2", 2, "2", "1211"
    4, "3", 2, "2", "1211" -> "121122"
    4, "3", 4, "2", "12111" -> "12112213"
    """

    assert(len(s) > 0)
    ret = utfb("")
    start = 0
    last_char = s[0]
    if len(s) == 1:
        ret = utfb("1")
        ret.append(last_char)
        return ret
    for j in range(1, len(s)):
        c = s[j]
        if c != last_char:
            # Start new sequence, record the last one
            ret.extend(utfb(str(j - start)))
            ret.append(last_char)
            start = j
        last_char = c
        if j == len(s) - 1:
            # Special handling for the last sequence
            ret.extend(utfb(str(j - start + 1)))
            ret.append(last_char)
    return ret


def look_and_say(k):
    """Return the kth number of the look and say problem.

    Idea: for each step, iterate through last string with a trailing pointer
    for the beginning of a sequence of the same number. Then write that out
    in new string.

    Time = ????, Space = O(1)

    """

    assert(k > 0)
    last_iter = utfb("1")
    for i in range(2, k + 1):
        last_iter = next_look_and_say(last_iter)
    return last_iter

