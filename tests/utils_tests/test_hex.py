import unittest
import random

from cryptopals.utils.hex import bytearray_to_hex_string, hex_string_to_bytearray, hex_string_to_int


class HexTests(unittest.TestCase):
    def test_hex_to_decimal(self):
        random.seed()
        rand_int = random.randint(0, 1000000)
        hexadecimal = hex(rand_int).split('x')[1]
        self.assertEqual(rand_int, hex_string_to_int(hexadecimal))

    def test_empty_string(self):
        """Empty hex string should return an empty bytearray."""
        result = hex_string_to_bytearray("")
        self.assertEqual(result, bytearray())

    def test_odd_length_padding(self):
        """Odd length string (e.g., 'F') is padded with a leading '0'."""
        # 'F' → padded to '0F' → byte 15
        result = hex_string_to_bytearray("F")
        self.assertEqual(result, bytearray([15]))

        # '1A3' → padded to '01A3' → bytes [1, 163]
        result = hex_string_to_bytearray("1A3")
        self.assertEqual(result, bytearray([0x01, 0xA3]))

    def test_even_length_single_byte(self):
        """Single byte represented by two hex characters."""
        result = hex_string_to_bytearray("FF")
        self.assertEqual(result, bytearray([255]))

        result = hex_string_to_bytearray("00")
        self.assertEqual(result, bytearray([0]))

    def test_even_length_multiple_bytes(self):
        """Multiple bytes from a longer even‑length hex string."""
        result = hex_string_to_bytearray("DEADBEEF")
        self.assertEqual(result, bytearray([0xDE, 0xAD, 0xBE, 0xEF]))

        result = hex_string_to_bytearray("010203")
        self.assertEqual(result, bytearray([1, 2, 3]))

    def test_case_insensitivity(self):
        result = hex_string_to_bytearray("deadbeef")
        self.assertEqual(result, bytearray([0xDE, 0xAD, 0xBE, 0xEF]))

        result = hex_string_to_bytearray("DeAdBeEf")
        self.assertEqual(result, bytearray([0xDE, 0xAD, 0xBE, 0xEF]))

    def test_valid_hex_string(self):
        self.assertEqual(
            hex_string_to_bytearray("0A1B2C"),
            bytearray([0x0A, 0x1B, 0x2C])
        )

    def test_lowercase_hex(self):
        self.assertEqual(
            hex_string_to_bytearray("0a1b2c"),
            bytearray([0x0A, 0x1B, 0x2C])
        )

    def test_mixed_case_hex(self):
        self.assertEqual(
            hex_string_to_bytearray("0A1b2C"),
            bytearray([0x0A, 0x1B, 0x2C])
        )

    def test_empty_string_hex_string_to_bytearray(self):
        self.assertEqual(
            hex_string_to_bytearray(""),
            bytearray()
        )

    def test_single_byte(self):
        self.assertEqual(
            hex_string_to_bytearray("FF"),
            bytearray([0xFF])
        )

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            hex_string_to_bytearray("ZZ12")

    def test_whitespace_in_string(self):
        with self.assertRaises(ValueError):
            hex_string_to_bytearray("0A 1B 2C")

    def test_prefix_0x_not_allowed(self):
        with self.assertRaises(ValueError):
            hex_string_to_bytearray("0x0A1B")

    def test_long_string(self):
        hex_str = "AA" * 1000
        expected = bytearray([0xAA] * 1000)
        self.assertEqual(
            hex_string_to_bytearray(hex_str),
            expected
        )

    def test_valid_bytearray(self):
        self.assertEqual(
            bytearray_to_hex_string(bytearray([0x0A, 0x1B, 0x2C])),
            "0a1b2c"
        )

    def test_empty_bytearray(self):
        self.assertEqual(
            bytearray_to_hex_string(bytearray()),
            ""
        )

    def test_single_byte_2(self):
        self.assertEqual(
            bytearray_to_hex_string(bytearray([0xFF])),
            "ff"
        )

    def test_all_zero_bytes(self):
        self.assertEqual(
            bytearray_to_hex_string(bytearray([0x00, 0x00])),
            "0000"
        )

    def test_mixed_values(self):
        self.assertEqual(
            bytearray_to_hex_string(bytearray([0x00, 0x7F, 0x80, 0xFF])),
            "007f80ff"
        )

    def test_long_bytearray(self):
        data = bytearray([0xAA] * 1000)
        expected = "aa" * 1000
        self.assertEqual(
            bytearray_to_hex_string(data),
            expected
        )

    def test_input_is_bytes(self):
        # Depending on your implementation, this may be allowed
        self.assertEqual(
            bytearray_to_hex_string(bytes([0x0A, 0x1B])),  # pyright: ignore
            "0a1b"
        )

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            bytearray_to_hex_string("0A1B")  # pyright: ignore
