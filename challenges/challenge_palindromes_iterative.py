# BASED ON https://www.w3schools.com/python/python_howto_reverse_string.asp


def is_palindrome_iterative(word):
    reversed = word[::-1]

    for count in range(len(word)):
        if word[count] != reversed[count]:
            return False

    if word == '':
        return False

    return True
