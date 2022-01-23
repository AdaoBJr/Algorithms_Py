def order_str(str):
    list_string = list(str)
    anagram_list = []

    while len(list_string) > 0:
        min = list_string[0]
        for f in list_string:
            if f < min:
                min = f
        anagram_list.append(min)
        list_string.remove(min)
    return anagram_list


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == '' or second_string == '':
        return False

    anagram1 = order_str(first_string)
    anagram2 = order_str(second_string)

    if anagram1 == anagram2:
        return True

    return False
