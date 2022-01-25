def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # Feito com ajuda do Esio Nacimento
    first_count = [0] * 256
    secound_count = [0] * 256

    for interavel in first_string:
        first_count[ord(interavel)] += 1

    for interavel in second_string:
        secound_count[ord(interavel)] += 1

    for interavel in range(256):
        if first_count[interavel] != secound_count[interavel] or len(
            first_string
        ) != len(second_string):
            return False

    return True
