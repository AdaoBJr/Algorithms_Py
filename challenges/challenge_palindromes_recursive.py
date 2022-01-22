def is_palindrome_recursive(word, low_index, high_index):
    # verificar string vazia:
    # https://www.horadecodar.com.br/2020/12/13/como-verificar-se-uma-string-esta-vazia-em-python/
    if not word or word is None or word[0] != word[-1]:
        return False
    # if word[0] != word[-1]:
    #  return False
    if len(word) <= 1 or (len(word) == 2 and word[0] == word[1]):
        return True
    # word[1:-1]: exclui a primeiro e a ultima posição
    return is_palindrome_recursive(word[1:-1], low_index, high_index)


# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
