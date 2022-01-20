def is_palindrome_recursive(word, low_index, high_index):
    # Testa se a palavra é nula ou difere o primeiro do último caracter
    if len(word) <= 0 or word[low_index] != word[high_index]:
        return False
    # Testa se a palavra após passar na checagem acima
    # tem dois ou mais caracteres o que indica que é um palindromo
    if len(word) <= 2:
        return True
    # Envia para a próxima chamada a própria função a palavra
    # sem o primeiro e último elemento até que passe em alguma verificação
    midst_word = word[1:-1]
    return is_palindrome_recursive(midst_word, 0, len(midst_word) - 1)
