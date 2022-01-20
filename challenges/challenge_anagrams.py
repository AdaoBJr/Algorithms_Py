def partition(str, low_index, high_index):
    i = low_index - 1
    pivot = str[high_index]
    for j in range(low_index, high_index):
        if str[j] <= pivot:
            i = i + 1
            str[i], str[j] = str[j], str[i]
    str[i + 1], str[high_index] = str[high_index], str[i + 1]

    return i + 1


# I'll try a quick sort :D
# btw, the course helped me to remember the function
def sort_string(str, low_index, high_index):
    if len(str) == 1:
        return str

    if low_index < high_index:
        partition_index = partition(str, low_index, high_index)

        sort_string(str, low_index, partition_index - 1)
        sort_string(str, partition_index + 1, high_index)


def is_anagram(first_string, second_string):
    first_str_to_arr = first_string.split()
    second_str_to_arr = second_string.split()
    first_length = len(first_str_to_arr) - 1
    secong_length = len(second_str_to_arr) - 1
    return sort_string(first_str_to_arr, 0, first_length) == sort_string(second_str_to_arr, 0, secong_length)
