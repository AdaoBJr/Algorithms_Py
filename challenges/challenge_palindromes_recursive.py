def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    palindrome = False
    if word == "":
        return palindrome
    if low_index >= high_index:
        palindrome = True
    elif word[low_index] == word[high_index]:
        palindrome = is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )
    return palindrome
