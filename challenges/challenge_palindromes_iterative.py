# Source https://www.portugal-a-programar.pt/forums/topic/72774
# -pal%C3%ADndrome-em-python-funcional/

def is_palindrome_iterative(word):
    if word == '':
        return False

    for a, b in zip(word, reversed(word)):
        if not a == b:
            return False
    return True
