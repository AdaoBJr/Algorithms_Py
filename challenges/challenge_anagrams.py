from string import ascii_lowercase as letters

# https://medium.com/@omadson/um-algoritmo-inteligente-para-descobrir-se-duas-palavras-s%C3%A3o-ou-n%C3%A3o-anagramas-9f4a108a63e


def primes(n):
    # função com formula para gerar números primos
    # no link encontra-se uma fórmula mais perfomática, porém
    # decidi usar essa pois lembro vagamente de já ter
    # estudado na época do colégio.
    return n**2 + n + 42


def letter_to_prime(letter):
    # converte as letras das palavras em um
    # correspondente primo ou produto de primos
    return primes(letters.index(letter))


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    two_words = (first_string, second_string)
    if "" in two_words:
        return False

    def string_to_prime(word):
        # funcao recursiva que utiliza da conversao
        # para primos, multiplicando os valores
        # e voltando, passando no restante da string
        # realizando a multiplicação até que a string termine
        if len(word) == 1:
            return letter_to_prime(word)
        return string_to_prime(word[0]) * string_to_prime(word[1:])

    if (string_to_prime(first_string) == string_to_prime(second_string)):
        return True
    return False
