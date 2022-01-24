# https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python


def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    reverse = word[::-1]
    if(not word):
        return False

    if word == reverse:
        return True

    return False
