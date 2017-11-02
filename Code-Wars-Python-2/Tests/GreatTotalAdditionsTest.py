import unittest
from GreatTotalAdditions import gta

class GtaTests(unittest.TestCase):
    def test(self):
        self.assertEqual(gta(7, 123489, 5, 67), 328804)
        self.assertEqual(gta(8, 12348, 47, 3639), 3836040)
        self.assertEqual(gta(9, 153456, 2339, 421876), 39456405)
        self.assertEqual(gta(1, 153456, 2339, 421876), 1)
        self.assertEqual(gta(2, 153456, 239, 42186), 9)
        self.assertEqual(gta(3, 53456, 2369, 4276), 121)
        self.assertEqual(gta(4, 3456, 239, 42176), 686)
        self.assertEqual(gta(5, 78432, 23578, 8532), 6525)
        self.assertEqual(gta(7, 123489, 5, 67), 328804)
        self.assertEqual(gta(3, 5528, 9870), 242)