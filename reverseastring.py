"""
Reverse a string
"""
import unittest

str_1 = "abc"
str_2 = "abdefghi"
str_3 = ""
str_4 = "a"

def reverse_string(s: str) -> str:
    if len(s) < 1:
        return s
    rev: str = ""
    for i in range(len(s)):
        rev += s[len(s)-1-i]
        # print(rev)
    # print(rev)
    return rev

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba", 'Should be "cba"')
        print("Test 01 Passed")

    def test_single_char(self):
        self.assertEqual(reverse_string("a"), "a", 'Should be "a"')
        print("Test 02 Passed")

    def test_empty(self):
        self.assertEqual(reverse_string(""), "", 'Should be "" ')
        print('Test 03 Passed')


unittest.main()