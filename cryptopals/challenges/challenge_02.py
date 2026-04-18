from cryptopals.utils.utils import xor_hex_strings


HEX_STRING_1 = "1c0111001f010100061a024b53535009181c"
HEX_STRING_2 = "686974207468652062756c6c277320657965"


def main():
    print("XORING HEX STRINGS:")
    print(HEX_STRING_1)
    print(HEX_STRING_2, end="\n\n")
    print("To get:")
    print(xor_hex_strings(HEX_STRING_1, HEX_STRING_2))
    return 0


if __name__ == "__main__":
    main()
