def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False

    if len(word) < 2:
        return True

    if low_index > high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# word = 'gg'
# print(is_palindrome_recursive(word, 0, len(word) - 1))
