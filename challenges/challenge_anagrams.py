def merge_sort(string):
    letter_list = list(string)
    list_length = len(letter_list)

    if list_length <= 1:
        return letter_list

    mid = list_length // 2

    list_left = merge_sort(letter_list[:mid])
    list_right = merge_sort(letter_list[mid:])

    return merge(list_left, list_right, letter_list.copy())


def merge(list_left, list_right, array_copy):
    i_left, i_right = 0, 0

    while (i_left < len(list_left) and i_right < len(list_right)):

        if list_left[i_left] <= list_right[i_right]:
            array_copy[i_left + i_right] = list_left[i_left]
            i_left += 1
        else:
            array_copy[i_left + i_right] = list_right[i_right]
            i_right += 1

    for i_left in range(i_left, len(list_left)):
        array_copy[i_left + i_right] = list_left[i_left]

    for i_right in range(i_right, len(list_right)):
        array_copy[i_left + i_right] = list_right[i_right]

    return array_copy


def is_anagram(first_string, second_string):
    first_list = merge_sort(first_string)
    second_list = merge_sort(second_string)

    if first_list == second_list:
        return True
    else:
        return False
