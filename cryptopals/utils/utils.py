from cryptopals.utils.base64 import bytes_to_base64
from cryptopals.utils.bytearrays import xor_bytearray_byte, xor_bytearrays
from cryptopals.utils.hex import (
    bytearray_to_hex_string,
    hex_string_to_bytearray
)
from cryptopals.utils.plaintext import get_dumb_plaintext_score


def hex_string_to_base64(hex_string: str) -> str:
    chomps = hex_string_to_bytearray(hex_string)
    return bytes_to_base64(chomps)


def xor_hex_strings(hex_string1: str, hex_string2: str) -> str:
    ba1 = hex_string_to_bytearray(hex_string1)
    ba2 = hex_string_to_bytearray(hex_string2)
    return bytearray_to_hex_string(xor_bytearrays(ba1, ba2))


def decode_hex_single_byte(hex_string: str) -> str:
    ba = hex_string_to_bytearray(hex_string)
    i = 1
    max_score = 0
    max_score_base64 = ""
    while i < 256:
        as_byte = i.to_bytes(1, 'big')
        decoded_maybe = xor_bytearray_byte(ba, as_byte)
        as_base64 = hex_string_to_base64(bytearray_to_hex_string(decoded_maybe))  # noqa: E501
        if get_dumb_plaintext_score(as_base64) > max_score:
            max_score = get_dumb_plaintext_score(as_base64)
            max_score_base64 = as_base64
        i += 1
    return max_score_base64
