# https://geekstocode.com/anagram-program-in-python/
# https://www.geeksforgeeks.org/python-program-to-check-whether-two-strings-are-anagram-of-each-other/


def is_anagram(first_string, second_string):
    # 256 caracteres - Código unicode ou tabela ASCII
    n_caracteres = 256
    count1 = [0] * n_caracteres
    count2 = [0] * n_caracteres
    for i in first_string:
        count1[ord(i)] += 1

    for i in second_string:
        count2[ord(i)] += 1

    for i in range(n_caracteres):
        if count1[i] != count2[i] or len(first_string) != len(second_string):
            return False

    return True
