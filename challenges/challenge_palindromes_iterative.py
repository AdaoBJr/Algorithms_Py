def is_palindrome_iterative(word):
    if not isinstance(word, str) or word == "":
        return False
    if word == word[::-1]:
        return True
    else:
        return False