def is_palindrome_iterative(word):
    if not word:
        return False

    primeira_letra = word[0]
    ultima_letra = word[-1]
    if primeira_letra != ultima_letra:
        return False
    elif len(word) <= 2:
        return True
    else:
        return is_palindrome_iterative(word[1:-1])
