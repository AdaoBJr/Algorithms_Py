# def is_palindrome_recursive(word, low_index, high_index):
# #      if word == '':
# #         return False

# #      elif len(word) == low_index:
# #         return True
 
# #      else:
# #         return word[::-1] == word


# def is_palindrome_recursive(word, low_index, high_index):
#     is_palindrome = ''
#     if high_index < low_index:
#         if word == '':
#             return False
#         else:
#             return is_palindrome == word
#     else: 
#         is_palindrome += word[high_index]
#         return is_palindrome_recursive(word, low_index, high_index - 1)


# def is_palindrome_recursive(word, low_index, high_index):
    
#     if word == '':
#         return False

#     elif len(word) == low_index:
#         return True
 
#     else:
#         is_palindrome = ''
#         if high_index == -1:
#             return 'batatinha'
#         else:
#             return word[high_index] + is_palindrome_recursive(word, low_index, high_index - 1)
        
    

# def is_palindrome_recursive(word, low_index, high_index):
    
#     if word == '':
#         return False

#     elif len(word) == low_index:
#         return True

#     # elif high_index == -1:
#     #     print(t)
#     else:
#         t = ''
#         if high_index != low_index:
#             t = word[low_index] == word[high_index]
#             is_palindrome_recursive(word, low_index + 1, high_index - 1)
#         return t

# Source https://www.portugal-a-programar.pt/forums/topic/72774-pal%C3%ADndrome-em-python-funcional/

# def is_palindrome_recursive(word, low_index, high_index):

#     if word == '':
#         return False

#     if len (word) == 1 or high_index < low_index:
#         return True

#     while low_index != high_index or low_index > high_index:
#         is_equal = word[low_index] == word[high_index]
#         word = word[low_index + 1: high_index]
#         high_index = len(word) - 1
#         return is_equal and is_palindrome_recursive (word, low_index, high_index)


def is_palindrome_recursive(word, low_index, high_index):

    if word == '':
        return False

    if len (word) == 1 or high_index < low_index:
        return True

    while low_index != high_index:
        is_equal = word[low_index] == word[high_index]
        
        if len(word) == 2:
            return is_equal
        else:
            word = word[low_index + 1: high_index]
            high_index = len(word) - 1
            return is_equal and is_palindrome_recursive (word, low_index, high_index)

# word = "reviver"
# # print(palindrome(word))
# print(is_palindrome_recursive(word, 0, len(word) - 1))
