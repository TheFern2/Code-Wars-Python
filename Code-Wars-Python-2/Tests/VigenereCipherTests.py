# -*- coding: utf-8 -*-

import unittest
from VigenereCipher import VigenereCipher

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

j = VigenereCipher('カタカナ', 'アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー')

class VigenereCipherTest(unittest.TestCase):
    def test(self):
        self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        self.assertEqual(c.decode('rovwsoiv'), 'codewars')
        self.assertEqual(c.encode('waffles'), 'laxxhsj')
        self.assertEqual(c.decode('laxxhsj'), 'waffles')
        self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')
        self.assertEqual(c.decode('CODEWARS'), 'CODEWARS')
        self.assertEqual(c.encode('it\'s a shift cipher!'), 'xt\'k o vwixl qzswej!')
        self.assertEqual(c.decode('xt\'k o vwixl qzswej!'), 'it\'s a shift cipher!')
        self.assertEqual(j.encode('ドモアリガトゴザイマス'),'ドオカセガヨゴザキアニ')
        self.assertEqual(j.decode('ドオカセガヨゴザキアニ'),'ドモアリガトゴザイマス')