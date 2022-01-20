def partition(arr, low_index, high_index):
    pivot = arr[high_index]
    item = low_index - 1

    for index in range(low_index, high_index):
        if arr[index] <= pivot:
            item = item + 1
            (arr[item], arr[index]) = (arr[index], arr[item])

    arr[item + 1], arr[high_index] = arr[high_index], arr[item + 1]

    return item + 1


# I'll try a quick sort :D
# this site helped me https://careerkarma.com/blog/python-quick-sort
def sort_string(arr, low_index, high_index):
    if low_index < high_index:
        pivot = partition(arr, low_index, high_index)

        sort_string(arr, low_index, pivot - 1)

        sort_string(arr, pivot + 1, high_index)


def is_anagram(first_string, second_string):
    first_str_to_arr = list(first_string)
    second_str_to_arr = list(second_string)

    first_length = len(first_str_to_arr) - 1
    secong_length = len(second_str_to_arr) - 1

    sort_string(first_str_to_arr, 0, first_length)
    sort_string(second_str_to_arr, 0, secong_length)

    separator = ''

    first_str_sorted = separator.join(first_str_to_arr)
    second_str_sorted = separator.join(second_str_to_arr)

    return first_str_sorted == second_str_sorted
