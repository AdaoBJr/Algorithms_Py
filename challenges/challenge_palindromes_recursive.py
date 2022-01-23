def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + list[0]


def is_palindrome_recursive(word, low_index, high_index):
    reversed = reverse(word)
    if word is None or word == "":
        return False
    elif len(word) < 2 and low_index == high_index:
        return True
    elif word == reversed:
        return True
    return False

