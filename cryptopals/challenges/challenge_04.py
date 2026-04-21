from cryptopals.utils.utils import decode_hex_strings_single_byte, dumb_read_file_strings


filepath = "/Users/adam/workspace/projects/python/cryptopals_python/cryptopals/files/challenge_04.txt"


def main():
    strings = dumb_read_file_strings(filepath)
    sorted_values = decode_hex_strings_single_byte(strings)
    for sol in sorted_values:
        print("Text: '{}'".format(sol.text), end=" ")
        print("Score: {}".format(sol.score), end=" ")
        print("Encoded Hex: {}".format(sol.encoded_hex))
    return 0

if __name__ == "__main__":
    main()
