def ordened(dale):
    # https://stackoverflow.com/questions/11964450/
    # python-order-a-list-of-numbers-without-built-in-sort-min-max-function
    new_string = []
    old_string = list(dale)
    while dale:
        mini = old_string[0]
        for x in old_string:
            if x < mini:
                mini = x
        new_string.append(mini)
        if len(old_string) != 1:
            old_string.remove(mini)
        else:
            break
    return ''.join(new_string)


def is_anagram(first_string, second_string):
    one = ordened(first_string)
    two = ordened(second_string)
    if one == two:
        return True
    return False
