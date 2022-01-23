import re


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_string = re.sub("[^0-9a-zA-Z]+", "", first_string)
    second_string = re.sub("[^0-9a-zA-Z]+", "", second_string)

    char_map_one = [0]*26
    char_map_two = [0]*26

    for index in range(len(first_string)):
        position = ord(first_string[index]) - ord('a')
        char_map_one[position] += 1

    for index in range(len(second_string)):
        position = ord(second_string[index]) - ord('a')
        char_map_two[position] += 1

    for index in range(26):
        if char_map_one[index] != char_map_two[index]:
            return False
    return True

# Para a resolução deste exercício usei como referência as soluções
# encontradas no endereço
# https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html
