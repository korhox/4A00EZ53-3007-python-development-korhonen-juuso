import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_get_first_index(self):
        self.assertEqual(get_first_index("kalle", "k"), 0)
        self.assertEqual(get_first_index("kalle", "a"), 1)
        self.assertEqual(get_first_index("kalle", "e"), 4)