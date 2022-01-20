def is_anagram(first_string, second_string):
    first_sorted = merge_sort(list(first_string))
    second_sorted = merge_sort(list(second_string))
    print(first_sorted)
    print(second_sorted)
    first_string_sorted = "".join(first_sorted)
    second_string_sorted = "".join(second_sorted)
    if first_string_sorted == second_string_sorted and len(
        first_string_sorted
    ) == len(second_string_sorted):
        return True
    return False


# SORTED RETIRADO DO COURSE DA TRYBE
def merge_sort(array):

    if len(array) <= 1:

        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1

        merged[left_cursor + right_cursor] = right[right_cursor]
        right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged