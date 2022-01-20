def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for w in first_string:
        if w not in second_string:
            return False