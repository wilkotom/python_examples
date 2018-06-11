# This exercise uses the following encoding: utf-8

import unittest
from session4 import palindrome


class TestPalindromeVerification(unittest.TestCase):
    def test_empty(self):
        self.assertIs(palindrome(''),False)

    def test_oxo(self):
        self.assertTrue(palindrome('oxo'))

    def test_panama(self):
        self.assertTrue(palindrome('A Man, A Plan, a Canal: Panama!'))

    def test_elba(self):
        self.assertTrue(palindrome("Able was I, ere I saw Elba 😁"))

    def test_seven(self):
        self.assertIs(palindrome('seven'), False)

    def test_nights(self):
        self.assertTrue(palindrome('1001N? 1001!'))

    def test_nonprint(self):
        self.assertIs(palindrome('\n1001 = 1001'),True)

    def test_emoji(self):
        self.assertIs(palindrome('(.)_(.)'), False)

    def test_inverted_smiley(self):
        self.assertIs(palindrome('|_^_|'), False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindromeVerification)
unittest.TextTestRunner(verbosity=2).run(suite)