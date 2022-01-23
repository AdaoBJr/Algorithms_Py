reverse = []


def is_palindrome_recursive(word, low_index, high_index):
    lista = list(word)

    if len(word) < 2:
        return word
    else:
        # reverse = ""
        reverse = (
            is_palindrome_recursive(word[1:], low_index, high_index - 1)
            + word[0]
        )

    if reverse == lista:
        True
