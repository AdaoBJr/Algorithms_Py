#  https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    array_first_string = list(first_string)
    array_second_string = list(second_string)

    first_array = sort_string(array_first_string)
    second_array = sort_string(array_second_string)

    if first_array == second_array:
        return True
    return False


def sort_string(array_word):
    for i in range(len(array_word)):
        minimum = i
        for j in range(i + 1, len(array_word)):
            if array_word[j] < array_word[minimum]:
                minimum = j
        print(array_word[minimum], array_word[i])
        aux = array_word[minimum]
        array_word[minimum] = array_word[i]
        array_word[i] = aux

    return array_word


if __name__ == "__main__":
    first_string = "pedar"
    second_string = "pedra"
    print(is_anagram(first_string, second_string))
