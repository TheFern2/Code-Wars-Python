import random
import time
import unittest
from BasicEncryption import encrypt

def encryptSol(text, rule):
    encrypted_text = ''
    for c in range(len(text)):
        encrypted_text += chr((ord(text[c]) + rule)%256)
    return encrypted_text

class BasicEncryptionRandomTest(unittest.TestCase):
    def test(self):
        #random.seed(int(time.time()))
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
        for i in range(50):
            text = ""
            for j in range(random.randint(1, 41)):
                text += chr(ord(chars[random.randint(0, len(chars) -1)]))
            rule = random.randint(0, 450)
            expected = encryptSol(text, rule)
            self.assertEqual(encrypt(text,rule), expected)