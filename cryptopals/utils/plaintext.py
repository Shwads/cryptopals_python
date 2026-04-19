monograms_frequency = {
    'a': 8.55, 'k': 0.81, 'u': 2.68,
    'b': 1.60, 'l': 4.21, 'v': 1.06,
    'c': 3.16, 'm': 2.53, 'w': 1.83,
    'd': 3.87, 'n': 7.17, 'x': 0.19,
    'e': 12.10, 'o': 7.47, 'y': 1.72,
    'f': 2.18, 'p': 2.07, 'z': 0.11,
    'g': 2.09, 'q': 0.10, 'h': 4.96,
    'r': 6.33, 'i': 7.33, 's': 6.73,
    'j': 0.22, 't': 8.94, '0': 0.00,
    '1': 0.00, '2': 0.00, '3': 0.00,
    '4': 0.00, '5': 0.00, '6': 0.00,
    '7': 0.00, '8': 0.00, '9': 0.00,
    '=': 0.00, '/': 0.00, '+': 0.00,
}


def score_bytearray(ba: bytearray) -> float:
    score = 0.0
    for byt in ba:
        if 65 <= byt <= 90 or 97 <= byt <= 122:
            score += 1
        elif not 32 <= byt <= 127:
            score -= 1
    return score


def get_dumb_plaintext_score(text: str) -> float:
    return sum(monograms_frequency.get(letter, -1) for letter in text.lower())


def bytearray_to_ascii(ba: bytearray) -> str:
    return ba.decode(encoding='ascii', errors='ignore')
