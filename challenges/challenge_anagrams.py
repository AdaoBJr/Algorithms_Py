# https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
# o site acima foi dica do Zózimo.

def sort(array):
    array = list(array)  # separa a string em uma lista
    new_list = []
    while array:
        minimum = array[0]
        for x in array:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        array.remove(minimum)
    return new_list


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    return sort(first_string) == sort(second_string)


first_string = "pedra"
second_string = "perda"
print(is_anagram(first_string, second_string))
