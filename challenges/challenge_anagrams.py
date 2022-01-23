def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == second_string:
        return True
    if len(first_string) != len(second_string):
        return False
    return False
