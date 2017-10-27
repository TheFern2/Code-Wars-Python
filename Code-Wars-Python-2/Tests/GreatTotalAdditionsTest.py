import unittest
from GreatTotalAdditions import gta

class GtaTests(unittest.TestCase):
    def test(self):
        self.assertEqual(gta(7, 123489, 5, 67), 328804)
        self.assertEqual(gta(8, 12348, 47, 3639), 3836040)
        self.assertEqual(gta(9, 153456, 2339, 421876), 39456405)
        self.assertEqual(gta(7, 32148, 59, 67), 387519)