def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string) or len(
            first_string) == 0 or len(second_string) == 0:
        print(first_string, second_string)
        return False
    if len(first_string) == 1 and len(second_string) == 1:
        return first_string == second_string
    for letter in first_string:
        if letter in second_string:
            newSecond = second_string.replace(letter, "", 1)
            return is_anagram(first_string[1:], newSecond)
        else:
            return False


# print(is_anagram("pedra", "perda"))
