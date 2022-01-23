# req 3 com a ajuda do Eder para realizar o sort
def bubble_sort(array):
    size = len(array)-1
    for position in range(size, 0, -1):
        for i in range(position):
            if array[i] > array[i+1]:
                temporary = array[i]
                array[i] = array[i+1]
                array[i+1] = temporary

    return array


# https://flexiple.com/convert-string-to-list-in-python/
def is_anagram(first_string, second_string):
    if first_string is None or second_string is None:
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string = list(first_string)
    second_string = list(second_string)

    first_string = bubble_sort(first_string)
    second_string = bubble_sort(second_string)

    if first_string == second_string:
        return True
    else:
        return False
        