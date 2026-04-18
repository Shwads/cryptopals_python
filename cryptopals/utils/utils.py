from cryptopals.utils.base64 import bytes_to_base64
from cryptopals.utils.bytearrays import xor_bytearrays
from cryptopals.utils.hex import (
    bytearray_to_hex_string,
    hex_string_to_bytearray
)


def hex_string_to_base64(hex_string: str) -> str:
    chomps = hex_string_to_bytearray(hex_string)
    return bytes_to_base64(chomps)


def xor_hex_strings(hex_string1: str, hex_string2: str) -> str:
    ba1 = hex_string_to_bytearray(hex_string1)
    ba2 = hex_string_to_bytearray(hex_string2)
    return bytearray_to_hex_string(xor_bytearrays(ba1, ba2))
