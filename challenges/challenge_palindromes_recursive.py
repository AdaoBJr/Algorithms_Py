def is_palindrome_recursive(word, low_index, high_index):
    # testa se a palavra é vazia
    if word == '':
        return False
    # testa se os index passados maior ou igual
    if low_index >= high_index:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
