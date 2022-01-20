# Source https://www.portugal-a-programar.pt/forums/topic/72774
# -pal%C3%ADndrome-em-python-funcional/

def is_palindrome_recursive(word, low_index, high_index):

    if word == '':
        return False

    if len(word) == 1 or high_index < low_index:
        return True

    while low_index != high_index:
        is_equal = word[low_index] == word[high_index]

        if len(word) == 2:
            return is_equal
        else:
            word = word[low_index + 1: high_index]
            high_index = len(word) - 1
            return is_equal and \
                is_palindrome_recursive(word, low_index, high_index)
