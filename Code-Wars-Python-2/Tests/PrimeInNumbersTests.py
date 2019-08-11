import unittest; from PrimesInNumbers import primeFactors2

class PrimeInNumbersTests(unittest.TestCase):
    def test(self):
        #self.assertEqual(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
        #self.assertEqual(primeFactors(7919), "(7919)")
        self.assertEqual(primeFactors2(987654321), "(3**2)(17**2)(379721)")