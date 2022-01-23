def order_string(string):
    abc = {}
    for l in string:
        if l in abc:
            abc[l] += 1
        else:
            abc[l] = 1

    return abc

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string) or first_string == '':
        return False
    order_first_string = order_string(first_string)
    order_second_string = order_string(second_string)
    if order_first_string == order_second_string:
        return True
    else: return False

print(is_anagram('amor', 'roma'))
print(is_anagram('ator', 'roma'))
print(is_anagram('amor', 'armor'))
print(is_anagram('', 'roma'))
print(is_anagram('ator', ''))