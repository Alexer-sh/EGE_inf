from itertools import product


def get_code_index(target):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(target)
    index = 0

    for l in range(1, length):
        index += len(alphabet) ** l

    for i, char in enumerate(target):
        pos = alphabet.index(char)
        index += pos * (len(alphabet) ** (length - i - 1))

    return index + 1


print(get_code_index("DEFFED"))