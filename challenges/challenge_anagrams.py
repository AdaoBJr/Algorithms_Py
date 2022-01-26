def merge_sort(string):
    letter_list = list(string)
    length = len(letter_list)

    if length <= 1:
        return letter_list

    mid = length // 2

    list_left, list_right = merge_sort(letter_list[:mid]), merge_sort(letter_list[mid:])

    return merge(list_left, list_right, letter_list.copy())


def merge(left, right, merged):
    index_left, index_right = 0, 0

    while (index_left < len(left) and index_right < len(right)):

        if left[index_left] <= right[index_right]:
            merged[index_left + index_right] = left[index_left]
            index_left += 1
        else:
            merged[index_left + index_right] = right[index_right]
            index_right += 1

    for index_left in range(index_left, len(left)):
        merged[index_left + index_right] = left[index_left]

    for index_right in range(index_right, len(right)):
        merged[index_left + index_right] = right[index_right]

    return merged


def is_anagram(first_string, second_string):
    first_list = merge_sort(first_string)
    second_list = merge_sort(second_string)
    
    if first_list == second_list:
        return True
    else:
        return False
