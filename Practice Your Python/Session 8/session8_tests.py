import unittest
from session8 import reachable_destination


class TestValidRoutes(unittest.TestCase):
    def test_nowhere_nowhere(self):
        self.assertIs(reachable_destination('', ''), False)

    def test_heathrow_nowhere(self):
        self.assertIs(reachable_destination('LHR', ''), False)

    def test_nowhere_leningrad(self):
        self.assertIs(reachable_destination('', 'LED'), False)

    def test_gatwick_leningrad(self):
        self.assertIs(reachable_destination('LGW', 'LED'), True)

    def test_manchester_leningrad(self):
        self.assertIs(reachable_destination('MAN', 'LED'), True)

    def test_heathrow_leningrad(self):
        self.assertIs(reachable_destination('LHR','LED'), False)

    def test_stanstead_leningrad(self):
        self.assertIs(reachable_destination('STD','LED'), False)

    def test_stanstead_toronto(self):
        self.assertIs(reachable_destination('YYZ','LED'), False)

    def test_heathrow_lunarcity7(self):
        self.assertIs(reachable_destination('LHR', 'LRX'), False)

    def test_leedsbradford_lunarcity7(self):
        self.assertIs(reachable_destination('LBA', 'LRX'), False)

    def test_seattle_manchester(self):
        self.assertIs(reachable_destination('SEA', 'MAN'), True)

    def test_manchester_lunarcity7(self):
        self.assertIs(reachable_destination('MAN','LRX'), True)


suite = unittest.TestLoader().loadTestsFromTestCase(TestValidRoutes)
unittest.TextTestRunner(verbosity=2).run(suite)

