import unittest
from GreatTotalAdditions import gta

class GtaTests(unittest.TestCase):
    def test(self):
        # self.assertEqual(gta(7, 123489, 5, 67), 328804)
        # self.assertEqual(gta(8, 12348, 47, 3639), 3836040)
        # self.assertEqual(gta(9, 153456, 2339, 421876), 39456405)
        # self.assertEqual(gta(1, 153456, 2339, 421876), 1)
        #self.assertEqual(gta(2, 153456, 2339, 421876), 9)
        #self.assertEqual(gta(5, 52456, 9639, 41876), 6786)
        #self.assertEqual(gta(5, 873456, 499, 31876), 8091)
        self.assertEqual(gta(3, 753456, 6339, 41876), 187)

