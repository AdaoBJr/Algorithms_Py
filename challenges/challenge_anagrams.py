# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions

def quicksort(string):
    if not string:
        return []
    return (quicksort([x for x in string[1:] if x < string[0]])
            + [string[0]] +
            quicksort([x for x in string[1:] if x >= string[0]]))


def is_anagram(first_string, second_string):
    if (
        len(first_string) != len(second_string)
            or first_string == "" or second_string == ""):
        return False
    sorted_string_one = quicksort(first_string)
    sorted_string_two = quicksort(second_string)
    if sorted_string_one == sorted_string_two:
        return True
    else:
        return False
