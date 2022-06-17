
import unittest

from string_helper import is_name


class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # with assertEqual you can check if two values the same:
        self.assertEqual(is_name("Ville Virtanen"), True)
        self.assertEqual(is_name("Ville virTanen", ignore_case=True), True)
        self.assertEqual(is_name("VillevirTanen", ignore_case=True), False)
        self.assertEqual(is_name("Ville VirtanEn"), False)
        self.assertEqual(is_name("ville Virtanen"), False)
        self.assertEqual(is_name("vIlle Virtanen"), False)
        self.assertEqual(is_name("Steve Jobs"), True)
        self.assertEqual(is_name("Steve jobs"), False)
        self.assertEqual(is_name("Steve jObs"), False)
        self.assertEqual(is_name("steve Jobs"), False)
        self.assertEqual(is_name("sTeve Jobs"), False)
        self.assertEqual(is_name("Sven Sthålberg"), True)
        self.assertEqual(is_name("Sven sthålberg"), False)
        self.assertEqual(is_name("Sven sthålberg", ignore_case=True), True)
        self.assertEqual(is_name("Oscar"), False)
        self.assertEqual(is_name("Dr. Miller"), False)
