def is_anagram(first_string, second_string):
    # http://excript.com/python/comparacao-de-string-python.html
    if first_string == '' or second_string == '':
        return False
    if first_string != second_string:
        return False
    return True
