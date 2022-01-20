def is_anagram(first_string, second_string):
    if first_string == second_string:
        return True
    if reversed(first_string) == reversed(second_string):
        return True

    return False
