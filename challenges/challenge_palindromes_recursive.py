def is_palindrome_recursive(word, low_index, high_index):
    if not len(word):
        return False

    if len(word) == 1 or high_index < low_index:
        return True

    if low_index != high_index:
        letters_matched = word[low_index] == word[high_index]

        # Verificção de palavras com tamanho par
        if len(word) == 2:
            return letters_matched

        return letters_matched \
            and is_palindrome_recursive(
                word[1:high_index], low_index, high_index-2)
