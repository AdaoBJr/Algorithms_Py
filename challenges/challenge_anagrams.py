"""
    Material consultado sobre ordenação em python
    https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
"""


def new_sort(string):
    string_copy = list(string)
    new_string = []

    while len(string_copy):
        minimum = string_copy[0]

        for item in string_copy:
            if item < minimum:
                minimum = item

        new_string.append(minimum)
        string_copy.remove(minimum)

    return new_string


def is_anagram(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
        or new_sort(first_string) != new_sort(second_string)
    ):
        return False

    return True


# if __name__ == "__main__":
#     first_string = ""
#     second_string = "perda"
#     print(f"{is_anagram(first_string, second_string)}")
