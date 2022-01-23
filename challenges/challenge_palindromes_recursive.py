# https://github.com/tryber/sd-10b-live-lectures/blob/lecture/35.2/exercicios/inverte.py
def inverte(lista):
    if not lista or len(lista) == 1:
        return lista
    return [lista[-1]] + inverte(lista[:-1])


def is_palindrome_recursive(word, low_index, high_index):
    string = inverte(list(word))

    if word == "" or None:
        return False

    return True if string == list(word) else False
