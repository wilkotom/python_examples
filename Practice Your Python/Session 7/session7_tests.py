import unittest
from session7 import validate


class TestCCValidator(unittest.TestCase):
    def test_empty(self):
        self.assertIs(validate(''), False)

    def test_zero(self):
        self.assertIs(validate('0'), True)

    def test_visa(self):
        self.assertIs(validate('4743903107345687'), True)

    def test_visa_no_nines(self):
        self.assertIs(validate('4743803307345687'), True)

    def test_mastercard(self):
        self.assertIs(validate('5490745468338088'), True)

    def test_amex(self):
        self.assertIs(validate('343539069275686'), True)

    def test_not_valid(self):
        self.assertIs(validate('4123412341234123'), False)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCCValidator)
unittest.TextTestRunner(verbosity=2).run(suite)