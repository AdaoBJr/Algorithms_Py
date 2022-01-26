def insertion_sort(string):
    letter_list = list(string)
    length = len(letter_list)

    for index in range(1, length):
        i = index

        while (i > 0 and letter_list[i] < letter_list[i - 1]):
            aux = letter_list[i]
            letter_list[i] = letter_list[i - 1]
            letter_list[i - 1] = aux
            i -= 1

    return letter_list;


def is_anagram(first_string, second_string):
    first_list = insertion_sort(first_string)
    second_list = insertion_sort(second_string)
    
    if first_list == second_list:
        return True
    else:
        return False
