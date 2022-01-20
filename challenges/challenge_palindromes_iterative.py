from audioop import reverse


def is_palindrome_iterative(word):
    if word == '':
        return False

    reverse_word = ''

    word_size = len(word) - 1
    for index in range(word_size, -1, -1):
        reverse_word += word[index]

    return word == reverse_word
