def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    # verificação de string vazia python "Gleison"
    if not word:
        return False
    # Metodo pythonic gleison

    return word == word[::-1]
