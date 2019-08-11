import unittest

def accum(s):
    out = []
    tempStr = ""
    for i in range(len(s)):
        for j in range(i+1):
            if j == 0:
                tempStr = s[i].upper()
            else:
                tempStr += s[i].lower()
        out.append(tempStr)
    print("-".join(out))
    return "-".join(out)

class MumblingTests(unittest.TestCase):
    def test(self):
        self.assertEqual(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")