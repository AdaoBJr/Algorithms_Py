def order_str(first, second):
    anagram = ''
    for f in first:
        for s in second:
            if f == s:
                anagram += s
    return anagram


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == '' or second_string == '':
        return False

    anagram = order_str(first_string, second_string)

    if first_string == anagram:
        return True

    return False

# print(is_anagram('', 'pato'))
