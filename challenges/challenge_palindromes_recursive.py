def is_palindrome_recursive(word, low_index, high_index):
    # verifica se word não é uma string vazia
    if not word:
        return False
    # verifica se o último elemento da string é igual ao primeiro...
    # Caso sejam, esta palavra PODE ser um palíndromo.
    if word[low_index] != word[high_index]:
        return False
    # verifica se low_index é maior ou igual o high_index. (Caso Base)
    if low_index >= high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# FONTE: encurtador.com.br/ehuSV
# Comparecimento ao plantão onde João me judou na formulação do caso base
