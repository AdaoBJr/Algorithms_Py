def palindrome(word, low_index, high_index):
    if high_index == 0:
        return word
    else:
        next = palindrome(word[:high_index], low_index + 1, high_index - 1)
        return word[high_index] + next


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == '':
        return False
    word1 = palindrome(word, low_index, high_index)
    if word1 == word:
        return True
    return False


# is_palindrome_recursive(word, 0, len(word) - 1)
# print(is_palindrome_recursive(word, 0, len(word) - 1))
