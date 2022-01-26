def is_palindrome_iterative(word):
    if not word:
        return False

    # https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
    return word == word[::-1]
