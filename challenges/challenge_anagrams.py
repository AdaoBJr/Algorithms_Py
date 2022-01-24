from challenges.helper_anagram import letter_to_prime


def is_anagram(first_string, second_string):
    # obtive ajuda do site 
    # https://medium.com/@omadson/um-algoritmo-inteligente-para-descobrir-se-duas-palavras-s%C3%A3o-ou-n%C3%A3o-anagramas-9f4a108a63e
    if first_string == '' or second_string == '':
        return False

    def word_to_prod(word):
        if len(word) == 1:
            return letter_to_prime(word)
        return word_to_prod(word[0]) * word_to_prod(word[1:])

    if word_to_prod(first_string) == word_to_prod(second_string):
        return True
    return False
