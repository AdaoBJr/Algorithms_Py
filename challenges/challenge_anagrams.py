def is_anagram(first_string, second_string):
    second_word = ""

    for i in range(len(second_string), 0, -1):
        second_word += second_string[i-1]

    if first_string == "":
        return False

    if first_string == second_word:
        return True
    
    return False

# print(is_anagram("pedra", "perda"))