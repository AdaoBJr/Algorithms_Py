from string import ascii_lowercase as letters

def primes(n):
        return 43142746595714191 + 5283234035979900*n

def letter_to_prime(letter):
    return primes(letters.find(letter))