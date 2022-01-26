def verify(string):
    original = list(string)
    new = []

    while string:
        ob = original[0]
        for i in original:
            if i < ob:
                ob = i
        new.append(ob)
        if len(original) != 1:
            original.remove(ob)
        else:
            break
    return ''.join(new)


def is_anagram(first_string, second_string):
    """ Faça o código aqui.. """
    first = verify(first_string)
    second = verify(second_string)

    if first == second:
        return True
    return False
