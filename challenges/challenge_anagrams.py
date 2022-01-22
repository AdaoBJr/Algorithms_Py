def is_anagram(first_string, second_string):
    """ A ord()função retorna um inteiro representando o caractere Unicode. """
    if first_string == "":
        return False

    if(len(first_string) != len(second_string)):
        return False

    count1 = [0] * 256
    count2 = [0] * 256

    for i in first_string:
        count1[ord(i)] += 1

    for i in second_string:
        count2[ord(i)] += 1

    for i in range(256):
        if count1[i] != count2[i]:
            return False

    return True
