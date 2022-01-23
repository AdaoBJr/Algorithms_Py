# Agradecimentos ao colega Jefferson Andrade
# pela ajuda no desenvolvimento da lógica

# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string_ordered, second_string_ordered = (
        merge_sort(list(first_string)),
        merge_sort(list(second_string)),
    )

    if first_string_ordered != second_string_ordered:
        return False

    return True


def merge_sort(str_arr):
    if len(str_arr) <= 1:
        return str_arr
    mid = len(str_arr) // 2

    left, right = merge_sort(str_arr[:mid]), merge_sort(str_arr[mid:])

    return merge(left, right, str_arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

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
