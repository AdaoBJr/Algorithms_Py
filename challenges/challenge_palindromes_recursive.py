def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False

    if low_index < high_index:
        # print(f"{word[low_index]} == {word[high_index]}")
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True


# if __name__ == "__main__":
#     word = "AGUA"
#     print(f"{is_palindrome_recursive(word, 0, len(word) - 1)}")
