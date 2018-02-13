import unittest
from session3 import decode


class TestPreT9Decoder(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(decode(''), '')

    def test_sos(self):
        self.assertEqual(decode('77776667777'), 'SOS')

    def test_mistaken_keypresses(self):
        self.assertEqual(decode('222220002'), 'A A')

    def test_number(self):
        self.assertEqual(decode('4444'), '4')

    def test_abc(self):
        self.assertEqual(decode('2 22 222'), 'ABC')

    def test_what_if_xkcd_75(self):
        self.assertEqual(decode('66 666 66 6 666 66 666426 666887777'), 'NONMONOGAMOUS')

    def test_full_sentence(self):
        self.assertEqual(decode('9996668802777330877727 733 304446602062999933033388555 55506663330477788337777'),
                         "YOU ARE TRAPPED IN A MAZE FULL OF GRUES")

    def test_multi_spaces(self):
        self.assertEqual(decode('0 0'), '  ')

    def test_zero(self):
        self.assertEqual(decode('00'), '0')

    def test_one(self):
        self.assertEqual(decode('1'), '1')

    def test_long_pause(self):
        self.assertEqual(decode('555666   66407288       777733'), 'LONG PAUSE')

    def test_pause_before_starting(self):
        self.assertEqual(decode('   728877773302233 3336667773307777827778444664'),'PAUSE BEFORE STARTING')


suite = unittest.TestLoader().loadTestsFromTestCase(TestPreT9Decoder)
unittest.TextTestRunner(verbosity=2).run(suite)
