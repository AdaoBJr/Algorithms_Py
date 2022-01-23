# Funcao reverse com recursividade retirada do course
def reverse(string):
    if len(string) < 2:
        return string
    return reverse(string[1:]) + string[0]


def is_palindrome_recursive(word, low_index, high_index):
    reversed = reverse(word)
    if word is None or word == "":
        return False
    if word == reversed:
        return True
    return False
