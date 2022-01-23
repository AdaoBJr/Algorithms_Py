def is_palindrome_recursive(word, low_index, high_index):
    if(word):
        if(high_index == 0 or (len(word) // 2) == low_index):
            return True

        if(word[low_index] == word[high_index]):
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
    else:
        return False
