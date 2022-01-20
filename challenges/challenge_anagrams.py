def is_anagram(first_string, second_string):
    if first_string != "" and second_string != "":
        first_string_in_order = order_string(first_string)
        second_string_in_order = order_string(second_string)
        if first_string_in_order == second_string_in_order:
            return True
        return False
    return False


# Inspirado no course, algoritmo de ordernação (inserção)
def order_string(string_to_order):
    string_list = list(string_to_order)
    for i in range(len(string_list)):
        current_value = string_list[i]
        current_position = i
        while (
            current_position > 0
            and string_list[current_position - 1] > current_value
        ):
            string_list[current_position] = string_list[current_position - 1]
            current_position = current_position - 1
        string_list[current_position] = current_value
    return "".join(string_list)
