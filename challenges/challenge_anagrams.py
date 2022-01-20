def quick_sort(lista):
    tam = len(lista)-1
    for passnum in range(tam, 0, -1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # Na tabela ascii cada letra possui um número e eles diferenciam
    # de maiscula pra minuscula
    # for push comment
    if (len(first_string) <= 1 and first_string == second_string):
        return True
    if first_string == second_string[::-1]:
        return True

    first_string = list(first_string)
    second_string = list(second_string)

    return quick_sort(first_string) == quick_sort(second_string)
