def is_palindrome_iterative(word):
    if word == '':
        return False
    low_index = 0
    high_index = len(word) - 1
    if len(word) < 2:
        return True
    for w in word:
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
    return True
