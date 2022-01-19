def is_palindrome_iterative(word):
    if not word:
        return False
    word_reverse = ''
    word_size = len(word) - 1
    while(word_size >= 0):
        word_reverse += word[word_size]
        word_size -= 1
    return word_reverse == word
