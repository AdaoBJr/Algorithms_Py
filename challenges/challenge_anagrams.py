def is_anagram(first_string, second_string):
    # feito com ajuda da Letycia barreto
    if first_string != second_string:
        return False
    if first_string == "" or second_string == "":
        return False
    if set(first_string.lower()) == set(second_string.lower()):
        return True
