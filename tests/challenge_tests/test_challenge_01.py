import unittest

from cryptopals.utils.utils import hex_string_to_base64


CHALLENGE_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
SOLUTION = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


class Challenge01Tests(unittest.TestCase):
    def test_challenge_01(self):
        base64_str = hex_string_to_base64(CHALLENGE_STRING)
        self.assertEqual(base64_str, SOLUTION)
