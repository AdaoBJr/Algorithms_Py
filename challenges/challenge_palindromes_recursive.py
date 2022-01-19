def checkPalindrome(word):
	if len(word) != 1:
		result = checkPalindrome(word[1:])+word[0]
		return result
	else:
		return word

def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if bool(word) == False: return False
    isPali = checkPalindrome(word)
    return isPali == word




