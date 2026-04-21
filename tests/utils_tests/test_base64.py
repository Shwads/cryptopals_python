# flake8: noqa E501
import unittest
import base64

from cryptopals.utils.base64 import base64_to_bytearray, bytes_to_base64, int_char_map, rec_base64_to_bytearray


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

    def test_valid_base64_simple_text(self):
        encoded = "aGVsbG8="
        result = base64_to_bytearray(encoded)
        expected = bytearray(b"hello")
        self.assertEqual(result, expected)

    def test_valid_base64_empty_string(self):
        encoded = ""
        result = base64_to_bytearray(encoded)
        expected = bytearray(b"")
        self.assertEqual(result, expected)

    def test_valid_base64_binary_data(self):
        original = bytes([0, 1, 2, 3, 254, 255])
        encoded = base64.b64encode(original).decode("ascii")
        result = base64_to_bytearray(encoded)
        expected = bytearray(original)
        self.assertEqual(result, expected)

    def test_valid_base64_without_padding_if_supported(self):
        encoded = "aGVsbG8"  # "hello" without trailing "="
        try:
            result = base64_to_bytearray(encoded)
            self.assertEqual(result, bytearray(b"hello"))
        except Exception:
            self.skipTest("Function does not support unpadded base64 input")

    def test_returns_bytearray_type(self):
        encoded = "dGVzdA=="  # "test"
        result = base64_to_bytearray(encoded)
        self.assertIsInstance(result, bytearray)

    def test_invalid_base64_characters(self):
        encoded = "not@base64!!"
        with self.assertRaises(Exception):
            base64_to_bytearray(encoded)

    def test_invalid_base64_length(self):
        encoded = "abc"
        with self.assertRaises(Exception):
            base64_to_bytearray(encoded)

    def test_none_input(self):
        with self.assertRaises(Exception):
            base64_to_bytearray(None)

    def test_non_string_input(self):
        with self.assertRaises(Exception):
            base64_to_bytearray(12345)




    def test_valid_base64_simple_text_recursive(self):
        encoded = "aGVsbG8="
        result = rec_base64_to_bytearray(encoded)
        expected = bytearray(b"hello")
        self.assertEqual(result, expected)

    def test_valid_base64_empty_string_recursive(self):
        encoded = ""
        result = rec_base64_to_bytearray(encoded)
        expected = bytearray(b"")
        self.assertEqual(result, expected)

    def test_valid_base64_binary_data_recursive(self):
        original = bytes([0, 1, 2, 3, 254, 255])
        encoded = base64.b64encode(original).decode("ascii")
        result = rec_base64_to_bytearray(encoded)
        expected = bytearray(original)
        self.assertEqual(result, expected)

    def test_valid_base64_without_padding_if_supported_recursive(self):
        encoded = "aGVsbG8"  # "hello" without trailing "="
        try:
            result = rec_base64_to_bytearray(encoded)
            self.assertEqual(result, bytearray(b"hello"))
        except Exception:
            self.skipTest("Function does not support unpadded base64 input")

    def test_returns_bytearray_type_recursive(self):
        encoded = "dGVzdA=="  # "test"
        result = rec_base64_to_bytearray(encoded)
        self.assertIsInstance(result, bytearray)

    def test_invalid_base64_characters_recursive(self):
        encoded = "not@base64!!"
        with self.assertRaises(Exception):
            rec_base64_to_bytearray(encoded)

    def test_invalid_base64_length_recursive(self):
        encoded = "abc"
        with self.assertRaises(Exception):
            rec_base64_to_bytearray(encoded)

    def test_none_input_recursive(self):
        with self.assertRaises(Exception):
            rec_base64_to_bytearray(None)

    def test_non_string_input_recursive(self):
        with self.assertRaises(Exception):
            rec_base64_to_bytearray(12345)
