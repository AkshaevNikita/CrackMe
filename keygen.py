import sys

def generate_key(name):
    word = 0
    for letter in name:
        word += ord(letter)
    return word ^ 0x5678 ^ 0x1234
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a name for registration. (For example: python3 keygen_my.py Brad)")
        sys.exit(1)
    else:
        print(generate_key(sys.argv[1].upper()))
