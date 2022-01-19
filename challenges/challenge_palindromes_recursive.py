from pickle import FALSE
def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if word[high_index] != word[low_index]:
        print("entrou aqui")
        return False

    if high_index  > low_index:
        low_index += 1
        high_index -= 1 
        return is_palindrome_recursive(word, low_index, high_index)
    return True
    # for i in range(0, len(word)-1):
    #     string += word[-i]
    # return string
    

print(is_palindrome_recursive("I", 0, len("i")-1))
