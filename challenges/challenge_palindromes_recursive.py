def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word or word[0] != word[-1]:
        return False
    if len(word) <= 1 or (len(word) == 2 and word[0] == word[1]):
        return True
    return is_palindrome_recursive(word[1:-1], word[0], word[-1])


# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python

# If a string has the first and last letters the same, and the remaining
# letters ([1:-1]) are a palindrome, it's a palindrome.
