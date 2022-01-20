# O algoritimo de ordenação foi o mesmo utilizado nos exemplos
# do curso da trybe.
def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    # print(left, right, merged)
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_string_ordened = merge_sort(list(first_string))
    second_string_ordened = merge_sort(list(second_string))

    return first_string_ordened == second_string_ordened


result = is_anagram('pedra', 'pesda')
print(result)
