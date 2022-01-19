def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if word[high_index] != word[low_index]:
        print("entrou aqui")
        return False

    if high_index > low_index:
        low_index += 1
        high_index -= 1
        return is_palindrome_recursive(word, low_index, high_index)
    return True
