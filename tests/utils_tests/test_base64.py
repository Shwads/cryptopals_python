import unittest

from cryptopals.utils.base64 import bytes_to_base64, int_char_map


class TestBytesToBase64(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
      
        cls.expected_map = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789+/"
        )
      
        for i, ch in enumerate(cls.expected_map):
            if int_char_map[i] != ch:
                raise ValueError(f"Mapping mismatch at index {i}: {int_char_map[i]} != {ch}")

    def test_empty_input(self):
        self.assertEqual(bytes_to_base64(bytearray()), "")

    def test_single_byte(self):
      
        self.assertEqual(bytes_to_base64(bytearray([0x00])), "AA==")
      
        self.assertEqual(bytes_to_base64(bytearray([0x01])), "AQ==")
      
        self.assertEqual(bytes_to_base64(bytearray([0xFF])), "/w==")
      
        self.assertEqual(bytes_to_base64(bytearray([0x49])), "SQ==")

    def test_two_bytes(self):
      
        self.assertEqual(bytes_to_base64(bytearray([0x00, 0x00])), "AAA=")
      
        self.assertEqual(bytes_to_base64(bytearray([0xFF, 0xFF])), "//8=")
      
        self.assertEqual(bytes_to_base64(bytearray([0x49, 0x27])), "SSc=")
      
        self.assertEqual(bytes_to_base64(bytearray([0xAB, 0xCD])), "q80=")

    def test_three_bytes(self):
      
        self.assertEqual(bytes_to_base64(bytearray([0x00, 0x00, 0x00])), "AAAA")
      
        self.assertEqual(bytes_to_base64(bytearray([0xFF, 0xFF, 0xFF])), "////")
      
        self.assertEqual(bytes_to_base64(bytearray([0x4D, 0x61, 0x6E])), "TWFu")
      
        self.assertEqual(bytes_to_base64(bytearray([0x49, 0x27, 0x6D])), "SSdt")

    def test_four_bytes(self):
      
        self.assertEqual(bytes_to_base64(bytearray([0x00, 0x00, 0x00, 0x00])), "AAAAAA==")
      
      
      
        self.assertEqual(bytes_to_base64(bytearray([0xFF, 0xFF, 0xFF, 0xFF])), "/////w==")
      
        self.assertEqual(bytes_to_base64(bytearray([0x31, 0x32, 0x33, 0x34])), "MTIzNA==")

    def test_odd_padding_handling(self):
      
      
        import base64
        data = bytearray([0x01, 0x02, 0x03, 0x04, 0x05])
        expected = base64.b64encode(data).decode()
        self.assertEqual(bytes_to_base64(data), expected)

    def test_random_bytes(self):
        import random
        import base64
        for _ in range(10):
            length = random.randint(0, 20)
            data = bytearray(random.getrandbits(8) for _ in range(length))
            expected = base64.b64encode(data).decode()
            self.assertEqual(bytes_to_base64(data), expected)

    def test_large_input(self):
        import base64
        data = bytearray(range(256)) * 4
        expected = base64.b64encode(data).decode()
        self.assertEqual(bytes_to_base64(data), expected)
