def reverse(word):
    if len(word) < 2:
        return word
    else:
        return reverse(word[1:]) + word[0]


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "":
        return False

    word_reverse = reverse(word)

    if (word_reverse == word):
        return True
    else:
        return False
