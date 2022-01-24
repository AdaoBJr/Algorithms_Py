from challenges.util_functions import is_anagram_recursive


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    return is_anagram_recursive(first_string, second_string, 0, 0)
