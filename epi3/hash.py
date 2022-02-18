"""Hash problems."""
from collections import Counter

def is_perm_palindrome(s):
    """
    Check whether string s can be permuted to form a palindrome.

    E.g., "edified" -> "deified"
    
    Idea: Order of the original word unimportant. All we need for a palindrome
    is that all the letters are in pairs (if even count) or all except one.
    Therefore put the individual chars as keys in a counter and then check if
    all (or all but one) pairs.
    Time: O(N), Space: O(N)
    """
    
    count = Counter()
    for char in s:
        count[char] += 1
    odd_counts = 0
    for char in count:
        if count[char] % 2 > 0:
            odd_counts += 1
    if odd_counts > 1:
        return False
    return True



