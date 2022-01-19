def is_palindrome_recursive(word, low_index, high_index):

    if len(word) == 0:
        return False
    elif len(word) == 1:
        return True
    elif word[low_index] == word[high_index] and len(word) == 2:
        return True
    else:
        return is_palindrome_recursive(word[1:-1], 0, len(word[1:-1]) - 1)
