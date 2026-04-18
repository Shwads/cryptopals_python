import unittest

from cryptopals.utils.bytearrays import xor_bytearrays


class TestXorBytearrays(unittest.TestCase):

    def test_basic_xor(self):
        a = bytearray([0x0F, 0xF0])
        b = bytearray([0xF0, 0x0F])
        expected = bytearray([0xFF, 0xFF])
        self.assertEqual(xor_bytearrays(a, b), expected)

    def test_xor_with_zero(self):
        a = bytearray([0x12, 0x34, 0x56])
        b = bytearray([0x00, 0x00, 0x00])
        self.assertEqual(xor_bytearrays(a, b), a)

    def test_xor_same_values(self):
        a = bytearray([0xAA, 0xBB, 0xCC])
        expected = bytearray([0x00, 0x00, 0x00])
        self.assertEqual(xor_bytearrays(a, a), expected)

    def test_empty_bytearrays(self):
        self.assertEqual(
            xor_bytearrays(bytearray(), bytearray()),
            bytearray()
        )

    def test_single_byte(self):
        a = bytearray([0xFF])
        b = bytearray([0x0F])
        expected = bytearray([0xF0])
        self.assertEqual(xor_bytearrays(a, b), expected)

    def test_mixed_values(self):
        a = bytearray([0x00, 0x7F, 0x80, 0xFF])
        b = bytearray([0xFF, 0x7F, 0x80, 0x00])
        expected = bytearray([0xFF, 0x00, 0x00, 0xFF])
        self.assertEqual(xor_bytearrays(a, b), expected)

    def test_long_bytearrays(self):
        a = bytearray([0xAA] * 1000)
        b = bytearray([0x55] * 1000)
        expected = bytearray([0xFF] * 1000)
        self.assertEqual(xor_bytearrays(a, b), expected)

    def test_different_lengths(self):
        a = bytearray([0x01, 0x02])
        b = bytearray([0x01])
        with self.assertRaises(ValueError):
            xor_bytearrays(a, b)

    def test_accepts_bytes_input(self):
        # Optional: adjust if your function does NOT support bytes
        a = bytes([0x0F, 0xF0])
        b = bytes([0xF0, 0x0F])
        expected = bytearray([0xFF, 0xFF])
        self.assertEqual(xor_bytearrays(a, b), expected)  # pyright: ignore
