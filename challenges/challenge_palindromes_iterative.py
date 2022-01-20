def is_palindrome_iterative(word):
    if not word:
        return False
    inverso = ""
    for i in range(len(word) - 1, -1, -1):
        inverso += word[i]
    if word == inverso:
        return True
    return False
