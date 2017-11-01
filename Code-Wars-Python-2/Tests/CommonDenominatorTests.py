import unittest
from CommonDenominator import convertFracts

class CommonDenominatorTest(unittest.TestCase):
    def test(self):
        # a = [[1, 2], [1, 3], [1, 4]]
        # b = [[6, 12], [4, 12], [3, 12]]
        # self.assertEqual(convertFracts(a), b)

        c = [[27115, 5262], [87546, 11111111], [43216, 255689]]
        d = [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
        self.assertEqual(convertFracts(c), d)