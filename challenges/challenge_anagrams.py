from challenges.helper_anagram import letter

def is_anagram(first_string, second_string):
    # obtive ajuda do site 
    # https://medium.com/@omadson/um-algoritmo-inteligente-para-descobrir-se-duas-palavras-s%C3%A3o-ou-n%C3%A3o-anagramas-9f4a108a63e
    if first_string == '' or second_string == '':
        return False

    def prod(word):
        if len(word) == 1:
            return letter(word)
        return prod(word[0]) * prod(word[1:])

    if prod(first_string) == prod(second_string):
        return True
    return False
