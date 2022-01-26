def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if len(word) == 1:
        return True

    if word[low_index] == word[high_index]:
        if len(word) == 2:
            return True

        sliced = word[1:-1]

        return is_palindrome_recursive(sliced, 0, len(sliced) - 1)

    return False


# word = "GG"
# is_palindrome_recursive("gg", 0, len(word) - 1)
