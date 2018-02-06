import unittest
from session2 import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_two(self):
        self.assertEqual(fibonacci(2), 1)

    def test_negative(self):
        self.assertEqual(fibonacci(-1), 0)

    def test_one_hundred(self):
        self.assertEqual(fibonacci(100), 354224848179261915075)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacci)
unittest.TextTestRunner(verbosity=2).run(suite)