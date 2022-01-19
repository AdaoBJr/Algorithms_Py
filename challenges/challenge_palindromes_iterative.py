def is_palindrome_iterative(word):
    if word == "":
        return False
    return word == word[::-1]

# print(is_palindrome_iterative(""))
# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
