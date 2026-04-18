import unittest

# Assume the function is defined in a module named 'base64_encoder'
from cryptopals.utils.base64 import bytes_to_base64, int_char_map

class TestBytesToBase64(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Verify the mapping is correct for the tests
        cls.expected_map = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789+/"
        )
        # Optional: check that int_char_map matches
        for i, ch in enumerate(cls.expected_map):
            if int_char_map[i] != ch:
                raise ValueError(f"Mapping mismatch at index {i}: {int_char_map[i]} != {ch}")

    def test_empty_input(self):
        """Empty bytearray should return empty string."""
        self.assertEqual(bytes_to_base64(bytearray()), "")

    def test_single_byte(self):
        """Single byte (8 bits) -> 2 base64 chars + 2 padding =."""
        # Byte 0x00 -> "AA=="
        self.assertEqual(bytes_to_base64(bytearray([0x00])), "AA==")
        # Byte 0x01 -> "AQ=="
        self.assertEqual(bytes_to_base64(bytearray([0x01])), "AQ==")
        # Byte 0xFF -> "/w=="
        self.assertEqual(bytes_to_base64(bytearray([0xFF])), "/w==")
        # Byte 0x49 (ASCII 'I') -> "SQ=="
        self.assertEqual(bytes_to_base64(bytearray([0x49])), "SQ==")

    def test_two_bytes(self):
        """Two bytes (16 bits) -> 3 base64 chars + 1 padding."""
        # 0x0000 -> "AAA="
        self.assertEqual(bytes_to_base64(bytearray([0x00, 0x00])), "AAA=")
        # 0xFFFF -> "//8="
        self.assertEqual(bytes_to_base64(bytearray([0xFF, 0xFF])), "//8=")
        # 0x4927 -> "SSc="
        self.assertEqual(bytes_to_base64(bytearray([0x49, 0x27])), "SSc=")
        # 0xABCD -> "q80="
        self.assertEqual(bytes_to_base64(bytearray([0xAB, 0xCD])), "q80=")

    def test_three_bytes(self):
        """Three bytes (24 bits) -> 4 base64 chars, no padding."""
        # 0x000000 -> "AAAA"
        self.assertEqual(bytes_to_base64(bytearray([0x00, 0x00, 0x00])), "AAAA")
        # 0xFFFFFF -> "////"
        self.assertEqual(bytes_to_base64(bytearray([0xFF, 0xFF, 0xFF])), "////")
        # "Man" -> "TWFu"
        self.assertEqual(bytes_to_base64(bytearray([0x4D, 0x61, 0x6E])), "TWFu")
        # 0x49276d -> "SSdt" (first part of challenge)
        self.assertEqual(bytes_to_base64(bytearray([0x49, 0x27, 0x6D])), "SSdt")

    def test_four_bytes(self):
        """Four bytes (32 bits) -> 5 base64 chars + 1 padding? Wait, actually 4 bytes = 32 bits, which is 5 full 6-bit groups + 2 leftover bits => 5 chars + 1 '=' padding.
        But standard base64 processes 3-byte blocks. For 4 bytes, we have one full block of 3 bytes (4 chars) and a second block of 1 byte (2 chars + 2 padding). Total 6 chars with 2 padding? Let's clarify:
        4 bytes = 32 bits -> 32/6 = 5.333 -> 6 base64 chars. Padding = (6 - (32+5)/6?) Actually formula: padding = (3 - (len(arr) % 3)) % 3. For len=4, 4%3=1 -> padding=2. So output length = ceil(4*8/6)=6 chars, last two are '='.
        So we test accordingly.
        """
        # 0x00000000 -> "AAAAAA=="
        self.assertEqual(bytes_to_base64(bytearray([0x00, 0x00, 0x00, 0x00])), "AAAAAA==")
        # 0xFFFFFFFF -> "//////8="? Let's compute: 4 bytes of 0xFF -> binary: 11111111 11111111 11111111 11111111
        # 6-bit groups: 111111 (63='/'), 111111 (63='/'), 111111 (63='/'), 111111 (63='/'), 111111 (63='/'), 111100 (60='8')? Wait that's 5 groups? Let's do properly:
        # 32 bits: group1: bits 0-5: 111111 -> '/'; group2: bits 6-11: 111111 -> '/'; group3: bits 12-17: 111111 -> '/'; group4: bits 18-23: 111111 -> '/'; group5: bits 24-29: 111111 -> '/'; group6: bits 30-31: only 2 bits, padded with zeros -> 110000? Actually bits 30-31 are '11', then pad with four zeros to make 6 bits: '110000' = 48 -> 'w'. Then padding: 2 '='. So result should be "//////w==". Let's confirm with known: Python's base64.b64encode(b'\xff\xff\xff\xff') -> b'/////w==' (that's 5 slashes? Wait Python gives: b'/////w==' which is 5 slashes? Let's test mentally: b'\xff\xff\xff\xff' has length 4. Python's output: '/////w==' (that's 5 '/' and then 'w=='). Actually 5 slashes? Let's count: 5 slashes + w + == = 8 chars. For 4 bytes, output length should be 6 chars plus 2 padding = 8. So 6 data chars: positions: 0-5. So we need 6 data chars. Python's '/////w==' has 5 slashes? That's only 5 data chars? Let's compute correctly: Use known fact: base64 of 4 bytes of 0xFF is '/////w==' (that's 5 slashes? Let's write: '/' '/' '/' '/' '/' 'w' '=' '=' -> that's 5 slashes? Actually count: characters: index0 '/',1 '/',2 '/',3 '/',4 '/',5 'w',6 '=',7 '='. That's 5 slashes? Index0-4 is 5 slashes, index5 is 'w'. So total 6 data chars: five '/' and one 'w'. That matches our earlier calculation? We had group5: all ones -> '/', group6: '110000' -> 'w'. So group1 to group5 are all '/'? That would be 5 slashes indeed. Group1-4 from first 24 bits give 4 slashes, group5 from next 6 bits (bits 24-29) gives another slash, group6 gives 'w'. So 5 slashes. So result '/////w==' is correct. So we test that.
        self.assertEqual(bytes_to_base64(bytearray([0xFF, 0xFF, 0xFF, 0xFF])), "/////w==")
        # Test a known string: "1234" -> ASCII '1'(0x31),'2'(0x32),'3'(0x33),'4'(0x34) -> base64: "MTIzNA=="
        self.assertEqual(bytes_to_base64(bytearray([0x31, 0x32, 0x33, 0x34])), "MTIzNA==")

    def test_odd_padding_handling(self):
        """The function currently expects input length to be even? Actually the function doesn't care; it works on bytes. But we should test a case where the input is not a multiple of 3."""
        # 5 bytes -> should have 1 padding
        # 0x0102030405 -> known? Compute manually or compare with Python's base64.
        import base64
        data = bytearray([0x01, 0x02, 0x03, 0x04, 0x05])
        expected = base64.b64encode(data).decode()
        self.assertEqual(bytes_to_base64(data), expected)

    def test_random_bytes(self):
        """Test several random byte arrays against Python's standard library."""
        import random
        import base64
        for _ in range(10):
            length = random.randint(0, 20)
            data = bytearray(random.getrandbits(8) for _ in range(length))
            expected = base64.b64encode(data).decode()
            self.assertEqual(bytes_to_base64(data), expected)

    def test_large_input(self):
        """Test a larger bytearray (e.g., 1000 bytes) for performance and correctness."""
        import base64
        data = bytearray(range(256)) * 4  # 1024 bytes
        expected = base64.b64encode(data).decode()
        self.assertEqual(bytes_to_base64(data), expected)

if __name__ == "__main__":
    unittest.main()
