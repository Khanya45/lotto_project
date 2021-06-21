import unittest
import random
import play


def randomnumbers():
    x = random.sample(range(1, 49), 6)
    print(x)
    return x


class Randomness(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 49


    def test_gen_age(self):
        randomnumbers()
        self.assertTrue(self.a >= 1 and self.b <=49)

