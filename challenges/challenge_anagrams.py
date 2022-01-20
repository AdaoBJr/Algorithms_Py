def is_anagram(first_string, second_string):
    first_string_sorted = sorted_string(first_string)
    second_string_sorted = sorted_string(second_string)
    print(first_string_sorted)
    print(second_string_sorted)

    if len(first_string_sorted) != len(second_string_sorted):
        return False
    
    if first_string_sorted == second_string_sorted:
        return True
       

def sorted_string(string):
    list_string = list(string)

    for i in range(len(list_string)):
        curr_value = list_string[i]
        curr_index = i

        while curr_index > 0 and list_string[curr_index - 1] > curr_value:
            list_string[curr_index] = list_string[curr_index - 1]
            curr_index = curr_index - 1
        list_string[curr_index] = curr_value
    return "".join(list_string)


print(is_anagram("amqqwoqr", "romqqqwa"))
