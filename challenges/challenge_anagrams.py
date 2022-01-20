def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # Na tabela ascii cada letra possui um número e eles diferenciam
    # de maiscula pra minuscula
    # for push comment

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    first_string = quick_sort(first_string)
    second_string = quick_sort(second_string)
    return first_string == second_string


def quick_sort(lista):
    for passnum in range(len(lista)-1, 0, -1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista
