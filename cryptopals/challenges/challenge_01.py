from cryptopals.utils.utils import hex_string_to_base64


CHALLENGE_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"  # noqa: E501 pylint: disable=line-too-long


def main():
    print("Translating hex:")
    print(CHALLENGE_STRING, end="\n\n")
    print("To base64:")
    print(hex_string_to_base64(CHALLENGE_STRING))
    return 0


if __name__ == "__main__":
    main()
