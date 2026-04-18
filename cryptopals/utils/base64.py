from enum import Enum


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
