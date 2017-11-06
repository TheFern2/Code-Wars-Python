import unittest
from MissingInArithmeticProgression import find_missing

class ProgressionTests(unittest.TestCase):
    def test(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
        self.assertEqual(find_missing([-1, -7, -10, -13, -16, -19, -22, -25, -28]), -4)
        self.assertEqual(find_missing([-1, 2, 5, 8, 11, 14, 17, 20, 26]), 23)
        self.assertEqual(find_missing([1, -2, -5, -8, -14, -17, -20, -23, -26]), -11)
        self.assertEqual(find_missing([12, 4, -4, -12, -20, -28, -44, -52, -60]), -36)
        self.assertEqual(find_missing([-13, 5, 14, 23, 32, 41, 50, 59, 68]), -4)