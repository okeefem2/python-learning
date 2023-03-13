# Convert base 10 number to base b
import unittest


def convert_to_base(n, b):
    if n < 0 or b < 2:
        raise
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        m = n % b
        n = n // b
        digits.insert(0, m)
    return digits


class TestConvertToBase(unittest.TestCase):
    def test_can_convert(self):
        assert convert_to_base(232, 5) == [1, 4, 1, 2]

