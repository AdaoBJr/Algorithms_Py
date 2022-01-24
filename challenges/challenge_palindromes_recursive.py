# REQUISITO FEITO COM A AJUDA DA ALESSANDRA REZENDE
def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[0] != word[-1]:
        return False
    if len(word) <= 1 or (len(word) == 2 and word[0] == word[1]):
        return True
    return is_palindrome_recursive(word[1:-1], low_index, high_index)