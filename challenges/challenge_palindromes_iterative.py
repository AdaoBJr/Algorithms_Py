from operator import truediv


def is_palindrome_iterative(word):
    if word is None or word == '':
        return False
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True
