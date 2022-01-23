def is_palindrome_recursive(word, low_index, high_index):
    if word is None or word == '':
        return False
    if len(word) < 2:
        return True
    if len(word) == 2 and word[low_index] == word[high_index]:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word[1:high_index], 0, high_index - 2)
    else:
        return False
