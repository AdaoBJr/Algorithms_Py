from challenges.helper_anagram import letter_to_prime


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    def word_to_prod(word):
        if len(word) == 1:
            return letter_to_prime(word)
        return word_to_prod(word[0]) * word_to_prod(word[1:])

    if word_to_prod(first_string) == word_to_prod(second_string):
        return True
    return False
