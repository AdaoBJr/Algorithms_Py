def is_palindrome_recursive(word, low_index, high_index):
    length = len(word) -1
    if word == "":
        return False
    if word[0] != word[length]:
        return False
    if length <= 1:
        return True
    
    return is_palindrome_recursive(word[1:length], 0, 0)

print(is_palindrome_recursive("GG",'', ''))
print(is_palindrome_recursive('A', '', ''))
print(is_palindrome_recursive("ANA",'', ''))
print(is_palindrome_recursive("SOCOS",'', ''))
print(is_palindrome_recursive("AGUA",'', ''))
print(is_palindrome_recursive("REVIVER",'', ''))
print(is_palindrome_recursive("COXINHA",'', ''))
print(is_palindrome_recursive('', '', ''))