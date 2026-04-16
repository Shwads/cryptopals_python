hex_digit_to_decimal = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15,
}


def hex_string_to_int(hex: str) -> int:
    exponent = 0
    total = 0
    for char in reversed(hex.lower()):
        try:
            total += hex_digit_to_decimal [char] * pow(16, exponent)
        except KeyError:
            raise ValueError(f"Invalid hexadecimal character {char}")
        exponent += 1
    return total


def hex_string_to_bytearray(hex: str) -> bytearray:
    chomps = bytearray()
    if len(hex) == 0:
        return chomps
    if len(hex) % 2 > 0:
        hex = '0' + hex

    s = 0
    e = 1
    while e < len(hex):
        chomp = hex_string_to_int(hex[s] + hex[e]).to_bytes()
        chomps.append(chomp[0])
        s += 2
        e += 2
    return chomps
