def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word or word[0] != word[-1]:
        return False
    if len(word) <= 1 or (len(word) == 2 and word[0] == word[1]):
        return True
    return (
        word == word[::-1]
    )  # inverte a string e compara. Retorna True se forem iguais.


# Encontre o reverso da string
# Verifique se o reverso e o original são iguais ou não.
# Se forem iguais, a string é palindromo.
# Se forem diferentes, a string não é palindromo.
# https://acervolima.com/programa-python-para-verificar-se-uma-string-e-palindromo-ou-nao/#:~:text=M%C3%A9todo%20usando%20a%20bandeira%3A%20Neste,%C3%A9%20um%20pal%C3%ADndromo%20ou%20n%C3%A3o.

# word = "I"
# print(word, is_palindrome_iterative(word))

# word = "GG"
# print(word, is_palindrome_iterative(word))

# word = "ANA"
# print(word, is_palindrome_iterative(word))

# word = "ESSE"
# print(word, is_palindrome_iterative(word))

# word = "SOCOS"
# print(word, is_palindrome_iterative(word))

# word = "REVIVER"
# print(word, is_palindrome_iterative(word))

# word = "AGUA"
# print(word, is_palindrome_iterative(word))

# word = ""
# print(word, is_palindrome_iterative(word))
