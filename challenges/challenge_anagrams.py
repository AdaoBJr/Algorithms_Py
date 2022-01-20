def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    n = 0
    if first_string == "" or second_string == "":
        return False
    for letra in second_string:
        primeira = first_string[n]
        if letra == primeira:
            n += 1
        else:
            return False
    return True


if __name__ == "__main__":
    is_anagram("pedra", "perda")
