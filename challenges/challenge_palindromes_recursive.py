def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    returns = False
    if word == "":
        return False
    if low_index >= high_index:
        return True
    if word[low_index] == word[high_index]:
        returns = is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return returns
