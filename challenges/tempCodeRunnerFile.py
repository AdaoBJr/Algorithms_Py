def order_string(string):
    unorder_string = string
    for i in range(len(unorder_string)):
        print(i)
        minimum = i
        for j in range(i + 1, len(unorder_string)):
            if unorder_string[j] < unorder_string[minimum]:
                minimum = j

        unorder_string[minimum], unorder_string[i] = unorder_string[i], unorder_string[minimum]

    return unorder_string


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string) or first_string == '':
        return False
    order_first_string = order_string(first_string)
    # order_second_string = order_string(second_string)
    # if order_first_string == order_second_string:
    #     return True
    return order_first_string



print(is_anagram('amor', 'roma'))