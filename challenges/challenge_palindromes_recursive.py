# for my reverse count https://stackoverflow.com/questions/869885/loop-backwards-using-indices-in-python

def make_palindrome(word, low_index, high_index):
    palindrome = ''
    if high_index == low_index:
        return palindrome + word[high_index]
    else:
        palindrome += word[high_index]
        return palindrome + make_palindrome(word, low_index, high_index - 1)


def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    return word == make_palindrome(word, low_index, high_index)
