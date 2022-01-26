def is_palindrome_recursive(word, low_index, high_index):
    finish_function = (high_index + 1) - (low_index + 1)
    if len(word) < 1 or not word:
        return False
    if finish_function > 1:
        if word[low_index] == word[high_index]:
            is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return False
    return True