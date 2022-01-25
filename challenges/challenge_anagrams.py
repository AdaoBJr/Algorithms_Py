def insertion_sort(word):
    word_list = []
    new_word = ''

    for i in word:
        word_list.append(i)

    for i in range(1, len(word)):
        current_value = word[i]
        current_position = i - 1

        while (
            current_position >= 0
            and
            current_value < word_list[current_position]
        ):
            word_list[current_position + 1] = word_list[current_position]
            current_position -= 1

        word_list[current_position + 1] = current_value

    for i in word_list:
        new_word += i

    return new_word


def is_anagram(first_string, second_string):
    first_word = insertion_sort(first_string)
    second_word = insertion_sort(second_string)

    if first_string == '' or second_string == '':
        return False

    if first_word == second_word:
        return True

    return False


print(is_anagram('', 'pedra'))
