def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    else:
        if low_index in range(len(word) + 1) and high_index in range(
            len(word) + 1
        ):
            if word[high_index - 1] != word[low_index - 1]:
                return False

            high_index -= 1
            low_index += 1
            is_palindrome_recursive(word, low_index, high_index)

    return True


if __name__ == "__main__":
    palavra = "huggo"
    print(is_palindrome_recursive(palavra, 0, len(palavra)))