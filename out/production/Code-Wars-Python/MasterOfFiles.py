import unittest
import re

def is_extension(ext):
    return bool(re.search(r'^[A-Za-z]+\.(ext.join)$'))

def is_audio(file_name):
    return bool(re.match(r'^[A-Za-z]+\.(mp3|flac|alac|aac)$', file_name))

def is_img(file_name):
    return bool(re.search(r'^[A-Za-z]+\.(jpg|jpeg|png|bmp|gif)$', file_name))

class MasterFileTests(unittest.TestCase):
    def test(self):
        self.assertEqual(is_audio("Nothing Else Matters.mp3"), False)
        self.assertEqual(is_audio("NothingElseMatters.mp3"), True)
        self.assertEqual(is_audio("DaftPunk.FLAC"), False)
        self.assertEqual(is_audio("DaftPunk.flac"), True)