def is_palindrome_recursive(word, low_index, high_index):
    # ref: https://stackoverflow.com/questions/952110/
    # recursive-function-palindrome-in-python
    if word == '':
        return False
    if len(word) <= 2 and word[0] == word[-1]:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1], low_index, high_index)
