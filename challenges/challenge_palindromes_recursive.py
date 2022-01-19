def is_palindrome_recursive(word, low_index, high_index):
    # https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
    if word == '':
        return False
    if low_index > high_index:
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))
    return False


# palindromo = "ANA"
# print(is_palindrome_recursive(palindromo, 0, len(palindromo) - 1))
