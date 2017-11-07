from random import random, randint, randrange, choice
from MissingInArithmeticProgression import find_missing2
import unittest

class MissingArithmeticProgressionRandomTests(unittest.TestCase):
    def fixture(self, bound, steps):
        a = randint(-bound, bound)
        c = randrange(3, bound + 3) * choice([-1, 1])
        good_sequence = [a + i * c for i in range(steps)]
        print(good_sequence)
        index = randrange(1, len(good_sequence)-1)
        expected = good_sequence[index]
        bad_sequence = good_sequence[:index] + good_sequence[index + 1:]
        #test.describe('Testing sequence of {} numbers'.format(steps))
        actual = find_missing2(bad_sequence)
        self.assertEqual(actual, expected)
        print("Actual ", actual, "Expected ", expected)

    def testRandom(self):
        for i in range(10):
            base = 1 + i * 5
            self.fixture(base, 10)
            # self.fixture(base, 100)
            # self.fixture(base, 1000)
            # self.fixture(base, 10000)
            # self.fixture(base, 100000)


if __name__ == '__main__':
    unittest.main()