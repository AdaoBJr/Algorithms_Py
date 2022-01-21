def is_anagram(first_string, second_string):
    first_string = selection_sort(first_string)
    second_string = selection_sort(second_string)
    if first_string == second_string:
        return True
    else:
        return False


""" def bubble_sort(word):
    word_list = list(word)
    word_size = len(word)
    for j in range(word_size - 1):
        for i in range(word_size - 1):
            if word_list[i] > word_list[i + 1]:
                word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
    return "".join(word_list) """


def selection_sort(word):
    word_list = list(word)
    word_size = len(word)
    for j in range(word_size - 1):
        min_index = j
        for i in range(j, word_size):
            if word_list[i] < word_list[min_index]:
                min_index = i
        if word_list[j] > word_list[min_index]:
            aux = word_list[j]
            word_list[j] = word_list[min_index]
            word_list[min_index] = aux
    return "".join(word_list)
