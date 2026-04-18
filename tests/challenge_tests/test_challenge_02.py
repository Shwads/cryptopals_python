import unittest

from cryptopals.utils.utils import xor_hex_strings


HEX_STRING_1 = "1c0111001f010100061a024b53535009181c"
HEX_STRING_2 = "686974207468652062756c6c277320657965"
SOLUTION = "746865206b696420646f6e277420706c6179"


class Challenge02Tests(unittest.TestCase):
    def test_challenge_02(self):
        solution = xor_hex_strings(HEX_STRING_1, HEX_STRING_2)
        self.assertEqual(solution, SOLUTION)
