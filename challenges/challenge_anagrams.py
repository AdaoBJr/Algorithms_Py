# https://www.kite.com/python/answers/how-to-sort-a-list-of-numbers-without-built-in-sort(),-min(),-max()-in-python
# https://careerkarma.com/blog/python-min-and-max/#:~:text=The%20Python%20min()%20function%20returns%20the%20lowest%20value%20in,the%20list%20were%20ordered%20alphabetically.
def is_anagram(first_string, second_string):
    if bool(first_string) and bool(second_string):
        word1 = sorting(first_string)
        word2 = sorting(second_string)

        return word1 == word2
    return False


def sorting(string):
    unsorted_list = list(string)
    sorted_list = []

    while unsorted_list:
        smallest = min(unsorted_list)
        sorted_list.append(smallest)
        unsorted_list.pop(unsorted_list.index(smallest))

    return "".join(sorted_list)
