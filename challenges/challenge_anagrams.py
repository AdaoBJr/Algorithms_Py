# www.edureka.co/community/50276/sort-numbers-without-using-built-functions-other-function
def orderList(list):
    new_list = []

    while list:
        minimum = list[0]  # arbitrary number in list
        for x in list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        list.remove(minimum)

    return new_list


# https://www.geeksforgeeks.org/python-program-convert-string-list/
def ConvertStrinToList(string):
    list1 = []
    list1[:0] = string
    return list1


def is_anagram(first_string, second_string):

    firstArr = orderList(ConvertStrinToList(first_string))
    secondArr = orderList(ConvertStrinToList(second_string))
    return firstArr == secondArr


if __name__ == "__main__":
    is_anagram('pedra', 'perda')
