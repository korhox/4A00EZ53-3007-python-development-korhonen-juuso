import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)

    def test_get_max(self):
        self.assertEqual(get_max(1, 2, 3), 3)
        self.assertEqual(get_max(3, 2, 1), 3)
        self.assertEqual(get_max(2, 3, 1), 3)
        self.assertEqual(get_max(2, 1, 3), 3)
        self.assertEqual(get_max(-1, 2, 3), 3)
        self.assertEqual(get_max(-3, -2, 1), 1)
        self.assertEqual(get_max(2, -3, 1), 2)
        self.assertEqual(get_max(-2, -1, -3), -1)

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("Saippuakauppias", False), False)
        self.assertEqual(is_palindrome("Saippuakauppias", True), True)
        self.assertEqual(is_palindrome("Abba", True), True)
        self.assertEqual(is_palindrome("Abba", False), False)
        self.assertEqual(is_palindrome("abba", False), True)
        self.assertEqual(is_palindrome("ABBA", False), True)
        self.assertEqual(is_palindrome("AbbA", False), True)