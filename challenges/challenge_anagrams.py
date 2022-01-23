def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    valor_a = list(first_string)
    a = "".join(sorted(valor_a))
    valor_b = list(second_string)
    b = "".join(sorted(valor_b))
    return a == b
