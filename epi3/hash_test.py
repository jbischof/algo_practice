import hash as hashlib
import unittest

class TestHash(unittest.TestCase):
    def test_is_perm_palindrome(self):
        a = 'rtthrghg' # Even number of letters, yes
        self.assertTrue(hashlib.is_perm_palindrome(a))
        b = 'rtthrghh' # Even number of letters, no
        self.assertFalse(hashlib.is_perm_palindrome(b))
        c = 'rtthrghhg' # Odd number of letters, yes 
        self.assertTrue(hashlib.is_perm_palindrome(c))

    def test_smallest_subarray_with_words(self):
        text = ["should", "not", "save", "the", "union", "or", "should", "save",
                "the", "best"]
        words = set(["save", "the", "union"])
        self.assertListEqual(
                list(hashlib.smallest_subarray_with_words(text, words)),
                [2, 4]
        )
