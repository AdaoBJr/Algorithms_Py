def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2 # retorna inteiro
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    # left ignora o primeira e right o segunda letra
    return merge(left, right, array.copy())


# misturar os dois arrays
def merge(left, right, merged):
    # LEFT E RIGHT ARRAY DE STRING
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    list_first_string = merge_sort(list(first_string))
    list_second_string = merge_sort(list(second_string))
    # list, é o split do js

    string_1 = "".join(list_first_string)
    string_2 = "".join(list_second_string)

    if string_1 == string_2 and len(string_1) == len(string_2):
        return True
    else:
        return False

# as strings são percorridas e percorrendo
# se algum valor for igual, a função é chamada novamente
# e ela para quando o tamanho do array for menor ou igual a 1
# tendo assim o novo array e depois juntando as letras
# para formar a nova palavra, executei com a palavra
# amor e roma e vi o roma de transformar em amor
# no final é comparado se são iguais as palavras
# e então a função para
# Agradecimentos:
# Pedro Henrique pelo auxilio no entendimento do course
# Função tirada do course Bloco 35.

# https://panda.ime.usp.br/panda/static/
# pythonds_pt/02-AnaliseDeAlgoritmos/
# ExemploDeDeteccaoDeAnagramas.html
