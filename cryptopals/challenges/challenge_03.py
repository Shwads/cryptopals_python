from cryptopals.utils.utils import decode_hex_single_byte


CHALLENGE_STRING = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"  # noqa: E501 pylint: disable=line-too-long


def main():
    print("Challenge 3 solution:")
    solutions = decode_hex_single_byte(CHALLENGE_STRING)
    for sol in solutions:
        print("Text: '{}'".format(sol.text), end=" ")
        print("Score: {}".format(sol.score))
    return 0


if __name__ == "__main__":
    main()
