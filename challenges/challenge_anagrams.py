# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
def quickSort(first_string):
    letter_list = list(first_string)
    quickSortHelper(letter_list, 0, len(letter_list) - 1)
    return letter_list


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def is_anagram(first_string, second_string):
    if (
        len(first_string) != len(second_string)
        or first_string == ""
        or second_string == ""
    ):
        return False

    sorted_f_word = quickSort(first_string)
    sorted_s_word = quickSort(second_string)
    return sorted_f_word == sorted_s_word
