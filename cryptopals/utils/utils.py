from collections.abc import Callable
from cryptopals.utils.base64 import bytes_to_base64
from cryptopals.utils.bytearrays import xor_bytearray_byte, xor_bytearrays
from cryptopals.utils.hex import (
    bytearray_to_hex_string,
    hex_string_to_bytearray
)
from cryptopals.utils.plaintext import (
    bytearray_to_ascii,
    get_dumb_plaintext_score,
    score_bytearray
)


class ScoredDecodedText:
    text: str
    score: float
    encoded_hex: str | None

    def __init__(
        self,
        *,
        text: str,
        score: float,
        encoded_hex: str | None = None,
    ):
        self.text = text
        self.score = score
        self.encoded_hex = encoded_hex


def hex_string_to_base64(hex_string: str) -> str:
    chomps = hex_string_to_bytearray(hex_string)
    return bytes_to_base64(chomps)


def xor_hex_strings(hex_string1: str, hex_string2: str) -> str:
    ba1 = hex_string_to_bytearray(hex_string1)
    ba2 = hex_string_to_bytearray(hex_string2)
    return bytearray_to_hex_string(xor_bytearrays(ba1, ba2))


def decode_hex_single_byte(hex_string: str) -> list[ScoredDecodedText]:
    ba = hex_string_to_bytearray(hex_string)
    i = 1
    solution_scores: list[ScoredDecodedText] = []
    while i < 256:
        as_byte = i.to_bytes(1, 'big')
        decoded_maybe = xor_bytearray_byte(ba, as_byte)
        solution = bytearray_to_ascii(decoded_maybe)
        solution_score = get_dumb_plaintext_score(solution) + score_bytearray(decoded_maybe)
        solution_scores.append(ScoredDecodedText(score=solution_score, text=solution))
        i += 1
    sorted_scores = sorted(solution_scores, key=lambda scored_sol: scored_sol.score)
    return sorted_scores[-5:]


def add_encoded_property_to_scored_decoded_text(
    hex_string: str
) -> Callable:
    def inner(
        sct: ScoredDecodedText,
    ):
        sct.encoded_hex = hex_string
        return sct
    return inner


def decode_hex_strings_single_byte(
    hex_strings: list[str],
) -> list[ScoredDecodedText]:
    """
    returns a dictionary mapping the index of string in the given list to
    it's returned score object from decode function
    """
    index_solution_map = {}
    solutions: list[ScoredDecodedText] = []
    for i in range(0, len(hex_strings)):
        scored_decoded_output = list(map(
            add_encoded_property_to_scored_decoded_text(hex_strings[i]),
            decode_hex_single_byte(hex_strings[i])
        ))
        index_solution_map[i] = scored_decoded_output
        solutions.extend(scored_decoded_output)
    # sorted_values = sorted(index_solution_map.values(), key=lambda val: val[0].score)
    sorted_values = sorted(solutions, key=lambda sct: sct.score)
    # print([sct.text for sct in sorted_values[-5:]])
    return sorted_values[-5:]
