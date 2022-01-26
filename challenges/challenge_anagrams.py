def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    str1 = ordena(first_string)
    str2 = ordena(second_string)

    if str1 == str2:
        return True
    else:
        return False    

# https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function


def ordena(word):
    word = list(word)
    new_list = []
    while word:
        st_letter = word[0]
        for letter in word:
            if letter < st_letter:
                st_letter = letter
        new_list.append(st_letter)
        word.remove(st_letter)
    return new_list