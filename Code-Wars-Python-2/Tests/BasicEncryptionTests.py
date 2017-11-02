import unittest
from BasicEncryption import encrypt

class BasicEncryptionTests(unittest.TestCase):
    def test(self):
        #self.assertEqual(encrypt("",1), "")
        #self.assertEqual(encrypt("a",1), "b")
        self.assertEqual(encrypt("please encrypt me",2), "rngcug\"gpet{rv\"og")