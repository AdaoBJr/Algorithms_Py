from string import ascii_lowercase as letters


def pr(number):
    return 43142746595714191 + 5283234035979900*number


def letter(letter):
    return pr(letters.find(letter))
