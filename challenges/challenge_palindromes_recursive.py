# https://datagy.io/python-palindrome/
# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
# acerto de procura/comparação de letra ajudada pelo Bugs

def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    
    if word[high_index] != word[low_index]:
        return False

    if high_index > low_index:
        high_index -= 1
        low_index += 1
        return is_palindrome_recursive(word, low_index, high_index)
    return True
