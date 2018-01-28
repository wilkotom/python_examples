import unittest
from session1 import redact

class TestRedaction(unittest.TestCase):

    def test_flamingo(self):
        self.assertEqual(redact("The Press Secretary's codename is Flamingo", ['flamingo', 'eagle']),
                         "The Press Secretary's codename is ****")

    def test_flamingo_and_eagle(self):
        self.assertEqual(redact("Flamingo and Eagle are meeting at 11:00", ['flamingo', 'eagle']),
                         "**** and **** are meeting at 11:00")

    def test_two_flamingos(self):
        self.assertEqual(redact("Flamingo hates that her codename is Flamingo", ['flamingo', 'eagle']),
                         "**** hates that her codename is ****")

    def test_no_match(self):
        self.assertEqual(redact("The weather has been clement for the time of year", ['flamingo', 'eagle']),
                         "The weather has been clement for the time of year")

    def test_empty_list(self):
        self.assertEqual(redact("Though I hear of a storm due to hit us later", []),
                                "Though I hear of a storm due to hit us later")

    def test_substring(self):
        self.assertEqual(redact("Flamingoland was my favourite theme park growing up", ['flamingo', 'eagle']),
                         "Flamingoland was my favourite theme park growing up")

    def test_empty_sentence(self):
        self.assertEqual(redact("", ['flamingo', 'eagle']), "")

    def test_empty_input(self):
        self.assertEqual(redact('', []), '')

if __name__ == '__main__':
    unittest.main()