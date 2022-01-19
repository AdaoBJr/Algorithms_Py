
# BUBBLE SORT - Quebrou na complexidade

# if len(first_string) != len(second_string): return False
#   listWord = list(word)

# sorted = False
# while not sorted:
#     for i in range(len(listWord)-1):
#         if listWord[i] > listWord[i+1]:
#             listWord[i+1], listWord[i] = listWord[i], listWord[i+1]
#             break
#     else:
#         sorted = True

# return "".join(listWord)

# SELECTION SORT

def sort(word):

    listWord = list(word)

    for i in range(len(listWord)):
        minimum = i
        for j in range(i + 1, len(listWord)):
            if(listWord[j] < listWord[minimum]):
                minimum = j

        listWord[minimum], listWord[i] = listWord[i], listWord[minimum]

    return "".join(listWord)


def is_anagram(first_string, second_string):

    if len(first_string) != len(second_string):
        return False

    first = sort(first_string)
    second = sort(second_string)
    return first == second
