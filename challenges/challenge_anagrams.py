# Função feita com a ajuda do Carlos Margato
# mas ainda não conseguimos resolver o tempo de execução
def bubble_sort(array):
    size = len(array)-1

    # percorra o array até o ultimo índice não ordenado
    for position in range(size, 0, -1):
        for i in range(position):
            if array[i] > array[i+1]:
                temporary = array[i]
                array[i] = array[i+1]
                array[i+1] = temporary

    return array


def is_anagram(first_string, second_string):
    if first_string is None or second_string is None:
        return False

    # transformar em letras minusculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # transformar str em lista
    first_string = list(first_string)
    second_string = list(second_string)

    first_string = bubble_sort(first_string)
    second_string = bubble_sort(second_string)

    # se o primeiro array for igual o segundo, true
    if first_string == second_string:
        return True
    else:
        return False
