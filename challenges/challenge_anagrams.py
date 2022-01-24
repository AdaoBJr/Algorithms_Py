def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if first_string[0] in second_string:
        string = second_string.replace(first_string[0], "", 1)
        return is_anagram(first_string[1:], string)
    else:
        return False
