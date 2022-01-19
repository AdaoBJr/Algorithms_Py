def is_palindrome_iterative(word):
    return word == word[::-1] if bool(word) is True else False