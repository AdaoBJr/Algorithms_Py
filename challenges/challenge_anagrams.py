def sorting(string):
    newArray = list(string)
    output = []
    while newArray:
        lower_letter = newArray[0]
        for letter in newArray:
            if letter < lower_letter:
                lower_letter = letter
        output.append(lower_letter)
        newArray.remove(lower_letter)
    return output


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    return sorting(first_string) == sorting(second_string)
