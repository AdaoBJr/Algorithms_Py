def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if word[0] != word[-1]:
        return False
    if len(word) == 2 and word[0] == word[-1]:
        return True
    if len(word) <= 1:
        return True
    return is_palindrome_recursive(word[1:-1], low_index, high_index)


# FONTE: encurtador.com.br/ehuSV
# FONTE: https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
# Comparecimento ao plantão onde João me judou na formulação do caso base
