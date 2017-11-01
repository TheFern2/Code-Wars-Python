import unittest
from MergedStringChecker import is_merge

class MergeStringCheckerTests(unittest.TestCase):
    def test(self):
        # self.assertTrue(is_merge('codewars', 'code', 'wars'))
        # self.assertTrue(is_merge('codewars', 'cdw', 'oears'))
        # self.assertTrue(not is_merge('codewars', 'cod', 'wars'))
        #self.assertTrue(not is_merge('', 'no', 'siree'))
        #self.assertTrue(not is_merge('codewars', 'code', 'warss'))
        self.assertTrue(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))
        #self.assertTrue(is_merge('Can we merge it? Yes, we can!', 'ane mr?e an!', 'C wege it Yes, wc'))