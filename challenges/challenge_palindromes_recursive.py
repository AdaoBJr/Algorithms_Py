def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index <= len(word) // 2 and high_index >= len(word) // 2:
        if word[high_index] == word[low_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
    return True
