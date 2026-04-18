hexit_to_decimal = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15,
}


int_to_hexit = {
    0: '0', 1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'a', 11: 'b',
    12: 'c', 13: 'd', 14: 'e', 15: 'f',
}


def hex_string_to_int(hex_str: str) -> int:
    exponent = 0
    total = 0
    for char in reversed(hex_str.lower()):
        try:
            total += hexit_to_decimal[char] * pow(16, exponent)
        except KeyError as e:
            raise ValueError(f"Invalid hexadecimal character {char}") from e
        exponent += 1
    return total


def hex_string_to_bytearray(hex_str: str) -> bytearray:
    chomps = bytearray()
    if len(hex_str) == 0:
        return chomps
    if len(hex_str) % 2 > 0:
        hex_str = '0' + hex_str

    s = 0
    e = 1
    while e < len(hex_str):
        chomp = hex_string_to_int(hex_str[s] + hex_str[e]).to_bytes(1, 'big')
        chomps.append(chomp[0])
        s += 2
        e += 2
    return chomps


def bytearray_to_hex_string(ba: bytearray) -> str:
    hex_str = ""
    for b in ba:
        first = int_to_hexit[b >> 4]
        last = int_to_hexit[b & 0b00001111]
        hex_str += (first + last)
    return hex_str
