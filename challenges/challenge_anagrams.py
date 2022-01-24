from string import ascii_lowercase as letters


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    
    def primes(n):
        return 43142746595714191 + 5283234035979900*n
    
    def letter_to_prime(letter):
        return primes(letters.index(letter))

    def word_to_prod(word):
        if len(word) == 1:
            return letter_to_prime(word)
        return word_to_prod(word[0]) * word_to_prod(word[1:])
    
    if word_to_prod(first_string) == word_to_prod(second_string):
        return True
    return False
