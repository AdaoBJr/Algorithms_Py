def is_palindrome_iterative(word):
    if word == '':
        return False
    word_invert = word[::-1]
    if word_invert == word:
        return True
    return False
