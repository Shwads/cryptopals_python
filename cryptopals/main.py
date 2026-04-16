import sys

from cryptopals.utils.hex import hex_string_to_int


def main():
    print("Hello World!")
    args = sys.argv[1:]
    if len(args) > 0:
        print(f"Got string: {args[0]}")
        print(f"hex value: {hex_string_to_int(args[0])}")


if __name__ == "__main__":
    main()
