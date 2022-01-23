# Source: 
# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions

def quicksort(string):
    if not string:
        return []
    return (quicksort([x for x in string[1:] if x < string[0]])
            + [string[0]] +
            quicksort([x for x in string[1:] if x >= string[0]]))


def is_anagram(first_string, second_string):
    first_string_ordered = quicksort(first_string)
    second_string_ordered = quicksort(second_string)
    if first_string_ordered == second_string_ordered:
        return True
    return False
