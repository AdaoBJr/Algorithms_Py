# https://pt.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/using-recursion-to-determine-whether-a-word-is-a-palindrome
def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1 or (len(word) == 2 and word[0] == word[1]):
        return True

    return is_palindrome_recursive(word[1:-1], low_index, high_index)


""" -Se a string só uma letra, é um palíndromo.
 -Caso contrário, comparar a primeira e última letra da sequência.
 -Se a primeira e última letra são diferentes,
então a string não é um palíndromo.
Do contrário, as primeiras e últimas letras são as mesmas.
Tire-as da string e determine se a sequência que permanece é um palíndromo.
Pegue a resposta para essa sequência menor e use-a
como a resposta para a sequência de caracteres original. """
