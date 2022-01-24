def sort_string(string):
    str_lst = list(string)

    for i in range(1, len(string)):
        if str_lst[i] < str_lst[i - 1]:
            str_lst[i], str_lst[i - 1] = str_lst[i - 1], str_lst[i]

    return ''.join(str_lst)


def is_anagram(first_string, second_string):
    str1 = sort_string(first_string)
    str2 = sort_string(second_string)

    print(str1, str2)

    if str1 == str2:
        return True
    return False


if __name__ == '__main__':
    print(is_anagram('amor', 'roma'))
