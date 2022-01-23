def is_palindrome_recursive(word, initialIndex, lastIndex):
    if word == '' or word[initialIndex] != word[lastIndex]:
        return False

    if initialIndex == lastIndex:
        return True

    if initialIndex < lastIndex + 1:
        return is_palindrome_recursive(word, initialIndex + 1, lastIndex - 1)

    return True
