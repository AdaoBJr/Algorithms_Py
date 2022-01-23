def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    elif word[low_index] != word[high_index]:
        return False
    elif len(word) <= 2:
        return True
    else:
        valor = word[1:][:-1]
        return is_palindrome_recursive(valor, 0, len(valor) - 1)

