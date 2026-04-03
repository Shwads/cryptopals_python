import unittest
import random

from cryptopals.lib.conversions import hex_string_to_int


class HexTests(unittest.TestCase):
    def test_hex_to_decimal(self):
        random.seed()
        rand_int = random.randint(0, 1000000)
        hexadecimal = hex(rand_int).split('x')[1]
        self.assertEqual(rand_int, hex_string_to_int(hexadecimal))
