def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left_cursor
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right_cursor
    return merged


def merge_sort(word):
    letter_list = list(word)
    if len(word) <= 1:
        return word
    middle = len(word) // 2
    left, right = merge_sort(
        letter_list[:middle]), merge_sort(letter_list[middle:])
    return merge(left, right, letter_list)


def is_anagram(first_string, second_string):
    if (
        len(first_string) != len(second_string)
            or first_string == "" or second_string == ""):
        return False
    sorted_string_one = merge_sort(first_string)
    sorted_string_two = merge_sort(second_string)

    if sorted_string_one == sorted_string_two:
        return True
    else:
        return False
