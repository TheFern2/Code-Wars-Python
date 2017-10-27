import unittest
from BestTravel import choose_best_sum

class Choose_best_sum_test(unittest.TestCase):
    def test(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEqual(choose_best_sum(230, 4, xs), 230)
        self.assertEqual(choose_best_sum(430, 8, xs), None)
        self.assertEqual(choose_best_sum(430, 5, xs), 430)
