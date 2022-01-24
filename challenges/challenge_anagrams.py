def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    
    def is_anagram_recursive(first_string, second_string, first_index, second_index):
        if first_index == len(first_string) or second_index == len(second_string):
            return True
        if first_string[first_index] != second_string[second_index]:
            return False
        if(first_index < len(first_string) and second_index < len(second_string)):
            return is_anagram_recursive(first_string, second_string, first_index + 1, second_index + 1)
        return True
    
    return is_anagram_recursive(first_string, second_string, 0, 0)
  
