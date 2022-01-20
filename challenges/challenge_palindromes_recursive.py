def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1:
        return True
    if word[low_index] == word[high_index]:
        cut_word = word[1:-1]
        if len(cut_word) == 0:
            return True
        return is_palindrome_recursive(cut_word, 0, -1)
    return False


# comentario para push
