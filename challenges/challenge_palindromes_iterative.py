def is_palindrome_iterative(word):
    if len(word) == 0 or not word:
        return False
    if word[::-1] == word:
        return True
    return False