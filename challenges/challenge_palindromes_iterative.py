def is_palindrome_iterative(word):
    if not word:
        return False
    inverso = ""
    for i in range(len(word) - 1, -1, -1):
        inverso += word[i]
    if word == inverso:
        return True
    return False


if __name__ == "__main__":

    assert is_palindrome_iterative("huggo") is False
    assert is_palindrome_iterative("") is False
    assert is_palindrome_iterative("ana") is True
    assert is_palindrome_iterative("socos") is True
