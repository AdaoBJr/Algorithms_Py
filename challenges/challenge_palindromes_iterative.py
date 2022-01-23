def is_palindrome_iterative(word):
    if word == "":
        return False
    
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    if reversed_word == word:
        return True
    else:
        return False

