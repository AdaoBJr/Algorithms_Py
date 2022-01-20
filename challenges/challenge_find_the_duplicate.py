def merge_sort(array):
    if len(array) <= 1:
        return array
    meio = len(array) // 2
    # divide o array em duas partes recursivamente
    left_list, right_list = merge_sort(array[:meio]), merge_sort(array[meio:])
    return merge(left_list, right_list, array.copy())


def merge(left_list, right_list, merged):
    index_left, index_right = 0, 0
    # insere os elementos de forma ordenada e incrementa o index
    while index_left < len(left_list) and index_right < len(right_list):
        if left_list[index_left] <= right_list[index_right]:
            merged[index_left + index_right] = left_list[index_left]
            index_left += 1
        else:
            merged[index_left + index_right] = right_list[index_right]
            index_right += 1

    # Como uma das partes do array pode terminar primeiro que a outra
    # é preciso adicioar os elementos restantes ao array que está sendo criado
    for index_left in range(index_left, len(left_list)):
        merged[index_left + index_right] = left_list[index_left]
    for index_right in range(index_right, len(right_list)):
        merged[index_left + index_right] = right_list[index_right]

    return merged


def find_duplicate(nums):
    if not nums:
        return False
    ordered_list = merge_sort(nums)
    index = 1
    for i in range(len(ordered_list) - 1):
        if (
            type(ordered_list[i]) == str
            or type(ordered_list[index]) == str
            or ordered_list[i] < 0
            or ordered_list[index] < 0
        ):
            return False
        if ordered_list[i] == ordered_list[index]:
            return ordered_list[i]
        index += 1
    return False