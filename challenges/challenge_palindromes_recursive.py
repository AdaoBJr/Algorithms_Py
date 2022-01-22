def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if word[low_index] != word[high_index]:
        # string e [] acessamos o valor da letra
        return False
    elif len(word) <= 2:
        return True
    else:
        return is_palindrome_recursive(word[1: -1], 0, -1)
        # pegando o valor da posição 1 do array e tirar o ultimo
        # se for :1 é ao contratio
        # o 0 sempre tira a primeira letra e o -1 a ultima
        # a função vai ficar passando até retornar true caso seja
        # palindromo, se não cai no false
# Agradecimentos ao Pedro Henrique pela ajuda
