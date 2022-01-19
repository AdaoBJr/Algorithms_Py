def is_palindrome_iterative(word):
    if word == '': 
        return False
    reverse_word = word[::-1]
    if reverse_word == word:
        return True
    return False
