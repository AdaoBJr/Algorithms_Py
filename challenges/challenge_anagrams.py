# https://github.com/tryber/sd-10b-live-lectures/blob/lecture/35.3/35_3_ordenacao_e_busca/1-progressao.py
def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        current_position = i - 1

        while (
            current_position >= 0 and current_value < array[current_position]
        ):
            array[current_position + 1] = array[current_position]
            current_position -= 1

        array[current_position + 1] = current_value

    return array


def is_anagram(first_string, second_string):
    first = insertion_sort(list(first_string))
    second = insertion_sort(list(second_string))

    # print(first)
    # print(second)

    if first == "" or second == "":
        return False

    if first != second:
        return False

    return True


# is_anagram("pedra", "perda")
