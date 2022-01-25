def merged(value):

    arrString = []
    primary_string = list(value)
    while value:
        half = primary_string[0]
        for range in primary_string:
            if range < half:
                half = range
        arrString.append(half)
        if len(primary_string) != 1:
            primary_string.remove(half)
        else:
            break
    return ''.join(arrString)


def is_anagram(first_string, second_string):
    first = merged(first_string)
    second = merged(second_string)
    if first == second:
        return True
    return False