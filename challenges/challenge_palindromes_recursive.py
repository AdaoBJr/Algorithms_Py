def is_palindrome_recursive(word, low_index, high_index):
    low_index = 0
    high_index = -1
    if not word:
        return False

    primeira_letra = word[low_index]
    ultima_letra = word[high_index]

    if primeira_letra != ultima_letra:
        return False
    elif len(word) <= 2:
        return True
    else:
        return is_palindrome_recursive(word[1:-1], low_index, high_index)
