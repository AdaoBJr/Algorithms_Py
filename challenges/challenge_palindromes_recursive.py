def is_palindrome_recursive(word, low_index, high_index):
    finish_function = high_index - low_index
    if len(word) < 1 or not word:
        return False
    if finish_function > 1:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return False
    if finish_function == 1:
        if word[low_index] != word[high_index]:
            return False
    return True