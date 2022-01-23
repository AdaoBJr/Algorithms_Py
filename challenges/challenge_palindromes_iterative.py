def is_palindrome_iterative(word):
    if word == "":
        return False
    
    empty_string = ''
    reversed_word = empty_string.join(reversed(word))
    if reversed_word == word:
        return True
    else:
        return False

# FONTE método reversed():
# https://www.tutorialsteacher.com/python/reversed-method
# FONTE método reversed():
# https://www.delftstack.com/pt/howto/python/reverse-a-string-python/