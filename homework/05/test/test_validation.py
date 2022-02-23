import unittest

from util.validation import is_date


class TestValidation(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("2022-10-10"))
        self.assertTrue(is_date("2022-12-31"))
        self.assertTrue(is_date("2022-01-31"))
        self.assertTrue(is_date("2022-10-31"))
        self.assertTrue(is_date("1999-05-12"))
        self.assertTrue(is_date("1989-05-02"))
        self.assertTrue(is_date("0009-05-02"))
        self.assertTrue(is_date("2009-10-10"))
        self.assertTrue(is_date("0000-05-02"))
        self.assertTrue(is_date("9999-12-31"))

        self.assertFalse(is_date("1999-1-12"))
        self.assertFalse(is_date("1989-05-1"))
        self.assertFalse(is_date("0009-05-00"))
        self.assertFalse(is_date("0009-00-02"))
        self.assertFalse(is_date("0009-00-02"))
        self.assertFalse(is_date("0000-05-00"))
        self.assertFalse(is_date("0009-00-00"))
        self.assertFalse(is_date("9999-00-00"))
