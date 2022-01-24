from challenges.helper_is_anagram import is_anagram_recursive


def is_anagram(first_string, second_string):
    if second_string == "" or first_string == "":
        return False
    return is_anagram_recursive(first_string, second_string, 0, 0)
