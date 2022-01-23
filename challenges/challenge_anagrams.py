def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == second_string:
        return True
    if len(first_string) != len(second_string):
        return False
    for first in first_string:
        check = False
        for second in second_string:
            if first == second:
                check = True
        if not check:
            return False
    return True
