import unittest
from session4 import palindrome


class TestPalindromeVerification(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(palindrome(''))

    def test_oxo(self):
        self.assertTrue(palindrome('oxo'))

    def test_panama(self):
        self.assertTrue(palindrome('A Man, A Plan, a Canal: Panama!'))

    def test_elba(self):
        self.assertTrue(palindrome("Able was I 'ere I saw Elba"))

    def test_seven(self):
        self.assertFalse(palindrome('seven'))

    def test_nights(self):
        self.assertTrue(palindrome('1001N? 1001!'))

suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindromeVerification)
unittest.TextTestRunner(verbosity=2).run(suite)