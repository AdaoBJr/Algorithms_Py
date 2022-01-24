def sort_string(string):
    string_list = list(string)

    for i in range(1, len(string)):
        if string_list[i] < string_list[i - 1]:
            string_list[i], string_list[i - 1] = string_list[i - 1] , string_list[i]

    return ''.join(string_list)


def is_anagram(first_string, second_string):
    str1 = sort_string(first_string)
    str2 = sort_string(second_string)

    print(str1, str2)

    if str1 == str2:
        return True
    return False


if __name__ == '__main__':
    print(is_anagram('amor', 'roma'))
