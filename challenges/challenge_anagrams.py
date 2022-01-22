""" A ord()função retorna um inteiro representando o caractere Unicode. """

CHARS = 256

def is_anagram(first_string, second_string):
    if first_string == "":
        return False

    if(len(first_string) != len(second_string)):
        return False

    count1 = [0] * CHARS
    count2 = [0] * CHARS

    for i in first_string:
        count1[ord(i)] += 1

    for i in second_string:
        count2[ord(i)] += 1

    for i in range(CHARS):
        if count1[i] != count2[i]:
            return False

    return True
