# Adaptado do artigo:
# https://acervolima.com/funcao-recursiva-para-verificar-se-uma-string-e-palindromo/
def is_palindrome_recursive(word, low_index, high_index):
    word = word.lower()

    if word == "" or word[low_index] != word[high_index]:
        return False

    if len(word) < 2:
        return True

    if low_index < high_index + 1:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True
