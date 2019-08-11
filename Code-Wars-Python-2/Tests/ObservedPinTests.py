import unittest
from ObservedPin import get_pins

class ObservedPinTests(unittest.TestCase):
    def test(self):
        expectations = [('8', ['5','7','8','9','0']),
                        ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                        ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

        for tup in expectations:
            self.assertEqual(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])