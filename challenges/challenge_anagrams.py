NO_OF_CHARS = 256

# Referência
# https://stackoverflow.com/questions/38024714/python-find-if-strings-are-anagram-of-each-other-string


def is_anagram(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return False

    count = [0] * NO_OF_CHARS

    for c1, c2 in zip(first_string, second_string):
        count[ord(c1)] += 1
        count[ord(c2)] -= 1
    return all(not c for c in count)
