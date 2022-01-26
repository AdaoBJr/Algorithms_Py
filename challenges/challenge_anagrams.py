def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    start = 0
    end = len(first_string)
    mid = start + end // 2
    return True
