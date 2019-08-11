import unittest

def find_missing_letter(chars):
    for i in range(len(chars)-1):
        temp1=(ord(chars[i]) + 1)
        temp2=(ord(chars[i+1]))
        if ord(chars[i]) + 1 != ord(chars[i+1]):
            return chr(ord(chars[i]) + 1)

class FindMissingLetterTests(unittest.TestCase):
    def test(self):
        self.assertEqual(find_missing_letter(['a','b','c','d','f']), 'e')
        self.assertEqual(find_missing_letter(['O','Q','R','S']), 'P')