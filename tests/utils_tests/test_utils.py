import unittest

from cryptopals.utils.utils import calculate_hamming_distance_strings


class UtilsTests(unittest.TestCase):
    def test_hamming_distance(self):
        STRING_1 = "this is a test"
        STRING_2 = "wokka wokka!!!"
        hamming_distance = calculate_hamming_distance_strings(STRING_1, STRING_2)
        self.assertEqual(hamming_distance, 37)
