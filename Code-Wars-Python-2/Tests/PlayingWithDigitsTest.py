import unittest
from PlayingWithDigits import dig_pow

class PlayingWithDigitsTests(unittest.TestCase):
    def test(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)