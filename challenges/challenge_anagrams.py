def order(string):
    list_string = [character for character in string]
    new_list_string = []
    while list_string:
        minimun = list_string[0]
        for character in list_string:
            if character < minimun:
                minimun = character
        new_list_string.append(minimun)
        list_string.remove(minimun)

    return new_list_string


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    # https://www.quora.com/How-do-I-sort-a-string-alphabetically-in-Python-without-using-the-sort-function
    if len(first_string) != len(second_string):
        return False
    else:
        list_first_string = order(first_string)
        list_second_string = order(second_string)

        return list_first_string == list_second_string
