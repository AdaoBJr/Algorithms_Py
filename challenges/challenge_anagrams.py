# def bubble_sort(lista):
#     tam = len(lista)-1
#     for passnum in range(tam, 0, -1):
#         for i in range(passnum):
#             if lista[i] > lista[i+1]:
#                 temp = lista[i]
#                 lista[i] = lista[i+1]
#                 lista[i+1] = temp
#     return lista

def merge_sort(array):
    # caso base: se já atingiu a menor porção (1)
    if len(array) <= 1:
        # retorne o array
        return array
    # calculo do pivot: índice que indica onde o array será particionado
    # no caso, metade
    mid = len(array) // 2
    # para cada metade do array
    # chama a função merge_sort de forma recursiva
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    # mistura as partes que foram divididas
    return merge(left, right, array.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    # enquanto nenhumas das partes é percorrida por completo
    while left_cursor < len(left) and right_cursor < len(right):

        # compare os dois itens das partes e insira no array de mistura o menor
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # a iteração acima irá inserir os elementos de forma ordenada

    # quando uma das partes termina, devemos garantir
    # que a outra sera totalmente inserida no array de mistura

    # itera sobre os elementos restantes na partição "esquerda"
    # inserindo-os no array de mistura
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # itera sobre os elementos restantes na partição "direita"
    # inserindo-os no array de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


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

    # gleison o algoritmo do bubble_sort tem muitos for
    # por este motivo a uma redução na performance
    # Não sei explicar o merge_sort apenas o bubble
    return merge_sort(first_string) == merge_sort(second_string)
