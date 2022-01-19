def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    # word_list = list(word)
    if not word:
        return False
    # i = len(word_list)
    # string_reversed = ""
    # while i > 0:
    #     string_reversed += word_list[i-1]
    #     i = i - 1

    return word == word[::-1]
