# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/


def is_palindrome_recursive(word, low_index, high_index):
    if bool(len(word)):

        # If there is only one character
        if low_index == high_index:
            return True

        # If first and last
        # characters do not match
        if word[low_index] != word[high_index]:
            return False

        # If there are more than
        # two characters, check if
        # middle substring is also
        # palindrome or not.
        if low_index < high_index + 1:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)

        return True

    else:
        return False
