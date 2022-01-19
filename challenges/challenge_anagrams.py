def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (len(first_string) != len(second_string)):
        return False
    return selection_sort(first_string) == selection_sort(second_string)


def selection_sort(array):
    # https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar
    # como um algoritmo de força bruta
    # percorre a estrutura exaustivamente
    # transforma a palavra em uma lista
    word = list(array)
    # percorre a lista
    for i in range(len(word)):
        minimum = i
        # itera sobre os elementos não ordenados
        for j in range(i + 1, len(word)):
            # testa se a a letra da posição J é igual a letra da posição minimo
            if word[j] < word[minimum]:
                # se true, atribui a posição de J como o valor minimo
                minimum = j
        # Faz as trocas das posições
        word[minimum], word[i] = word[i], word[minimum]

    return word
