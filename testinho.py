
def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if bool(word) == False: return False
    # isPali = checkPalindrome(word)
    # return isPali == word
    isPali = ''
    final = ''
    if len(word) != 1:
        result = is_palindrome_recursive(word[1:],1, 2)+word[0]
        isPali =  result
    else:
        final = word

    return isPali == final


print(is_palindrome_recursive('ANA',1, 23))