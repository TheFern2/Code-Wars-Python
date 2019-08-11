import unittest

def printHello():
    return "Hello World!"

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(printHello(), "Hello World!")