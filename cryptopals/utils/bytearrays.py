from cryptopals.utils.constants import (
    ERROR_MESSAGE_LENGTH_NOT_EQUAL,
    ERROR_MESSAGE_MANY_BYTES
)


def xor_bytearrays(ba1: bytearray, ba2: bytearray) -> bytearray:
    if len(ba1) != len(ba2):
        raise ValueError(
            ERROR_MESSAGE_LENGTH_NOT_EQUAL.format("xor_bytearrays")
        )
    output = bytearray()
    for b1, b2 in zip(ba1, ba2):
        output.append(b1 ^ b2)
    return output


def xor_bytearray_byte(ba: bytearray, b: bytes) -> bytearray:
    if len(b) == 1:
        ERROR_MESSAGE_MANY_BYTES.format(
            "xor_bytearray_byte",
            len(b)
        )
    ba2 = bytearray(b * len(ba))
    return xor_bytearrays(ba, ba2)
