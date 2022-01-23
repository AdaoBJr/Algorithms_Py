def order_string(string):
    abcdary = {}
    for l in string:
        if l in abcdary:
            abcdary[l] += 1
        else:
            abcdary[l] = 1
    return abcdary


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string) or first_string == '':
        return False
    order_first_string = order_string(first_string)
    order_second_string = order_string(second_string)
    if order_first_string == order_second_string:
        return True
    else: 
        return False