def is_palindrome_recursive(word, low_index, high_index):
    finish_function = high_index - low_index
    if len(word) < 1:
        return False
    if finish_function > 0:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return False
    return True
