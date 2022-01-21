# https://geekstocode.com/anagram-program-in-python/
# https://www.geeksforgeeks.org/python-program-to-check-whether-two-strings-are-anagram-of-each-other/

def is_anagram(first_string, second_string):
    # 256 caracteres - Código unicode ou tabela ASCII
    NO_OF_CHARS = 256
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    for i in first_string:
        count1[ord(i)] += 1

    for i in second_string:
        count2[ord(i)] += 1

    if len(first_string) != len(second_string):
        return False

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False

    return True
