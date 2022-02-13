import strings
from strings import utfb
import unittest

class TestStrings(unittest.TestCase):
    def test_spreadsheet_encoding(self):
        self.assertEqual(strings.spreadsheet_encoding("D"), 4)
        self.assertEqual(strings.spreadsheet_encoding("AA"), 27)
        self.assertEqual(strings.spreadsheet_encoding("ZZ"), 702)

    def test_reverse_range(self):
        b = utfb('Bob likes Alice')
        strings.reverse_range(b, 4, 8)
        self.assertEqual(b, utfb('Bob sekil Alice'))

    def test_reverse_words(self):
        b = utfb('Bob likes Alice')
        strings.reverse_words(b)
        self.assertEqual(b, utfb('Alice likes Bob'))
        b = utfb('Bob likes Alice')
        strings.reverse_words2(b)
        self.assertEqual(b, utfb('Alice likes Bob'))
        # Space at beginning and end, different spacing between words
        b = utfb(' Bob likes  Alice ')
        strings.reverse_words2(b)
        self.assertEqual(b, utfb(' Alice  likes Bob '))

    def test_look_and_say(self):
        self.assertEqual(strings.next_look_and_say(utfb("1")), utfb("11")) 
        self.assertEqual(strings.next_look_and_say(utfb("11")), utfb("21")) 
        self.assertEqual(strings.next_look_and_say(utfb("11233")), utfb("211223")) 
        self.assertEqual(strings.next_look_and_say(utfb("211223")), utfb("12212213")) 
        self.assertEqual(strings.look_and_say(8), utfb("1113213211"))

                
