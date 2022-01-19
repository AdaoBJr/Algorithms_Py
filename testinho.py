from re import I, M


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # mudança
    listWord = list(first_string)

    for i in range(len(listWord)):
      minimum = i
      for j in range(i + 1, len(listWord)):
        if(listWord[j] < listWord[minimum]):
          minimum = j

      listWord[minimum], listWord[i] = listWord[i], listWord[minimum]

    return "".join(listWord)


    # if len(first_string) != len(second_string): return False

    # sorted = False
    # while not sorted:
    #     for i in range(len(listWord)-1):
    #         if listWord[i] > listWord[i+1]:
    #             listWord[i+1], listWord[i] = listWord[i], listWord[i+1]
    #             break
    #     else:
    #         sorted = True

    # return "".join(listWord)


print(is_anagram('zxya', 'amdsor'))