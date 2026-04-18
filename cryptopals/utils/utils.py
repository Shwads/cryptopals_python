from cryptopals.utils.base64 import bytes_to_base64
from cryptopals.utils.hex import hex_string_to_bytearray


def hex_string_to_base64(hex_string: str) -> str:
    chomps = hex_string_to_bytearray(hex_string)
    return bytes_to_base64(chomps)
