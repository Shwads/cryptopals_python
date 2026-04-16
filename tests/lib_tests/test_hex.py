import unittest
import random

from cryptopals.utils.hex import hex_string_to_bytearray, hex_string_to_int


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
        """The function should handle both uppercase and lowercase hex digits."""
        result = hex_string_to_bytearray("deadbeef")
        self.assertEqual(result, bytearray([0xDE, 0xAD, 0xBE, 0xEF]))
        
        result = hex_string_to_bytearray("DeAdBeEf")
        self.assertEqual(result, bytearray([0xDE, 0xAD, 0xBE, 0xEF]))
