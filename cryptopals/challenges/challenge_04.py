from cryptopals.utils.utils import decode_hex_strings_single_byte


filepath = "/Users/adam/workspace/projects/python/cryptopals_python/cryptopals/files/challenge_04.txt"
def read_file_strings(filename: str) -> list[str]:
    strings = []
    with open(filename) as textfile:
        for line in textfile:
            strings.append(line[:-1])
    return strings


def main():
    strings = read_file_strings(filepath)
    sorted_values = decode_hex_strings_single_byte(strings)
    for sol in sorted_values:
        print("Text: '{}'".format(sol.text), end=" ")
        print("Score: {}".format(sol.score), end=" ")
        print("Encoded Hex: {}".format(sol.encoded_hex))
    return 0

if __name__ == "__main__":
    main()
