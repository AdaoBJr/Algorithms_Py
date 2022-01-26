def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word or word[low_index] != word[-1]:
        return False
    if len(word) == 1:
        return True
    elif len(word) == 2 and word[low_index] == word[1]:
        return True
    return is_palindrome_recursive(word[1:-1], low_index, high_index)
