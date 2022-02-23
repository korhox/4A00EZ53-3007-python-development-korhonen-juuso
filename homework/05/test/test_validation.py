import unittest

from util.validation import *


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

    def test_is_email(self):
        self.assertTrue(is_email("jussi.pohjolainen@tuni.fi"))
        self.assertTrue(is_email("juuso.m.korhonen@tuni.fi"))
        self.assertTrue(is_email("juuso.korhonen@bittivirta.fi"))
        self.assertTrue(is_email("juuskor@me.com"))
        self.assertTrue(is_email("juuso@korho.fi"))
        self.assertTrue(is_email("cheap@gmail.com"))
        self.assertTrue(is_email("something@mysub.munsivu.fi"))
        self.assertTrue(is_email("gang@subs.sub.munsivu.fi"))
        self.assertTrue(is_email("sdf@sdf4yhs.com"))
        self.assertTrue(is_email("sdf@sdf4yhs.sdwhdf"))

        self.assertFalse(is_email("jussi.pohjolainen(at)tuni.fi"))
        self.assertFalse(is_email("jussi.pohjolainen.tuni.fi"))
        self.assertFalse(is_email("jussi.pohjolainentuni.fi@"))
        self.assertFalse(is_email("jussi.pohjolainentuni@fi"))
        self.assertFalse(is_email("jussi.pohjolainentuni.fi"))
        self.assertFalse(is_email("sdf@sdf4yhs"))
        self.assertFalse(is_email("sdfsdf4yhs.sdwhdf"))
        self.assertFalse(is_email("sdfsdf4yhs"))

    def test_is_personal_id(self):
        self.assertTrue(is_personal_id("131052-308T"))
        self.assertTrue(is_personal_id("120464-121C"))
