#VQV
from collections import Counter


def is_anagram(first_string, second_string):
    return Counter(first_string) == Counter(second_string)

    # print(is_anagram("roma","amor"))
    # https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
