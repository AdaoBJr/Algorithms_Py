def sort_string(string):
    array_char = [char for char in string]
    for i in range(len(array_char)):
        min = i

        for j in range(i + 1, len(array_char)):
            if array_char[j] < array_char[min]:
                min = j

        array_char[min], array_char[i] = array_char[i], array_char[min]

    return ''.join(array_char)


def is_anagram(first_string, second_string):
    if not len(first_string) or not len(second_string):
        return False
    return sort_string(first_string) == sort_string(second_string)
