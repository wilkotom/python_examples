import unittest
from session5 import scrabble_score


class TestScrabbleScorer(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(scrabble_score(''),0)

    def test_expedia(self):
        self.assertEqual(scrabble_score('EXPEDIA'),0)

    def test_syzygy(self):
        self.assertEqual(scrabble_score('syzygy'), 25)

    def test_hexangular(self):
        self.assertEqual(scrabble_score('hexangular'), 0)

    def test_lect(self):
        self.assertEqual(scrabble_score('lect'), 0)

    def test_ionizer(self):
        self.assertEqual(scrabble_score('ionizer'), 66)

    def test_jezebel(self):
        self.assertEqual(scrabble_score('jezebel'), 0)

    def test_invalid_input(self):
        self.assertEqual(scrabble_score('Boom!'), 0)


suite = unittest.TestLoader().loadTestsFromTestCase(TestScrabbleScorer)
unittest.TextTestRunner(verbosity=2).run(suite)