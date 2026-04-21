import struct


int_char_map = {
    0: 'A', 16: 'Q', 32: 'g', 48: 'w',
    1: 'B', 17: 'R', 33: 'h', 49: 'x',
    2: 'C', 18: 'S', 34: 'i', 50: 'y',
    3: 'D', 19: 'T', 35: 'j', 51: 'z',
    4: 'E', 20: 'U', 36: 'k', 52: '0',
    5: 'F', 21: 'V', 37: 'l', 53: '1',
    6: 'G', 22: 'W', 38: 'm', 54: '2',
    7: 'H', 23: 'X', 39: 'n', 55: '3',
    8: 'I', 24: 'Y', 40: 'o', 56: '4',
    9: 'J', 25: 'Z', 41: 'p', 57: '5',
    10: 'K', 26: 'a', 42: 'q', 58: '6',
    11: 'L', 27: 'b', 43: 'r', 59: '7',
    12: 'M', 28: 'c', 44: 's', 60: '8',
    13: 'N', 29: 'd', 45: 't', 61: '9',
    14: 'O', 30: 'e', 46: 'u', 62: '+',
    15: 'P', 31: 'f', 47: 'v', 63: '/',
}


char_int_map = {
    'A': 0, 'Q': 16, 'g': 32, 'w': 48,
    'B': 1, 'R': 17, 'h': 33, 'x': 49,
    'C': 2, 'S': 18, 'i': 34, 'y': 50,
    'D': 3, 'T': 19, 'j': 35, 'z': 51,
    'E': 4, 'U': 20, 'k': 36, '0': 52,
    'F': 5, 'V': 21, 'l': 37, '1': 53,
    'G': 6, 'W': 22, 'm': 38, '2': 54,
    'H': 7, 'X': 23, 'n': 39, '3': 55,
    'I': 8, 'Y': 24, 'o': 40, '4': 56,
    'J': 9, 'Z': 25, 'p': 41, '5': 57,
    'K': 10, 'a': 26, 'q': 42, '6': 58,
    'L': 11, 'b': 27, 'r': 43, '7': 59,
    'M': 12, 'c': 28, 's': 44, '8': 60,
    'N': 13, 'd': 29, 't': 45, '9': 61,
    'O': 14, 'e': 30, 'u': 46, '+': 62,
    'P': 15, 'f': 31, 'v': 47, '/': 63,
}


def bytes_to_base64(arr: bytearray) -> str:
    if len(arr) == 0:
        return ''
    bit_count = len(arr) * 8
    v = 3 - ((len(arr) * 4) % 3)
    padding = v if v != 3 else 0
    pad_chars = '=' * padding
    bit_count += padding
    chomps = arr[:]
    # always put an extra byte at the end so can index
    # N + 1 without going out of bounds
    chomps.extend(bytearray(1))
    base64_str = ""

    for bit in range(0, bit_count, 6):
        index = bit // 8
        remainder = bit % 8
        curr_byte = chomps[index]
        next_byte = chomps[index+1]
        joined = (curr_byte << 8) | next_byte
        # Taking the pointers in our word as p1 and p2
        # we find the distance between p2 and the required shift
        # by taking the offset from the byte start (bit // 8)
        # plus the length of the character from the end.
        shift = 16 - (remainder + 6)
        num = (joined >> shift) & 63
        base64_char = int_char_map[num]
        base64_str += base64_char
    return base64_str + pad_chars


def base64_to_bytearray(base64_str: str) -> bytearray:
    # return rec_base64_to_bytearray(base64_str)
    if base64_str == "":
        return bytearray()
    end = -1
    padding = 0
    while base64_str[end] == '=':
        padding += 1
        end -= 1
    bit_count = ((len(base64_str) - padding) * 6) - (padding * 2)
    output = bytearray()
    for i in range(0, bit_count, 8):
        curr_index = i // 6
        offset = i % 6
        byte_start = char_int_map[base64_str[curr_index]] << 2
        byte_end = char_int_map[base64_str[curr_index+1]]
        curr_byte_start = (((255 >> offset) & byte_start) << offset)
        curr_byte_end = (byte_end >> (4 - offset))
        full_byte = curr_byte_start | curr_byte_end
        output.append(full_byte)
    return output


def rec_base64_to_bytearray(base64_str: str) -> bytearray:
    if base64_str == "":
        return bytearray()
    end = -1
    padding = 0
    while base64_str[end] == '=':
        padding += 1
        end -= 1
    bit_count = ((len(base64_str) - padding) * 6) - (padding * 2)
    def inner(bit_start: int, ba: bytearray) -> bytearray:
        if not bit_start + 8 <= bit_count:
            return ba
        curr_char_index = bit_start // 6
        byte_start = char_int_map[base64_str[curr_char_index]] << 2
        byte_end = char_int_map[base64_str[curr_char_index+1]]
        offset = bit_start % 6
        curr_byte_start = (((255 >> offset) & byte_start) << offset)
        curr_byte_end = (byte_end >> (4 - offset))
        ba.append(curr_byte_start | curr_byte_end)
        return inner(bit_start + 8, ba)
    return inner(0, bytearray())
