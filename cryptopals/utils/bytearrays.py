from cryptopals.utils.constants import ERROR_MESSAGE_LENGTH_NOT_EQUAL


def xor_bytearrays(ba1: bytearray, ba2: bytearray) -> bytearray:
    if len(ba1) != len(ba2):
        raise ValueError(ERROR_MESSAGE_LENGTH_NOT_EQUAL.format("function xor_bytearrays"))
