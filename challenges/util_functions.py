def is_anagram_recursive(fst_string, sec_string, fst_index, sec_index):
    if fst_index == len(fst_string) or sec_index == len(sec_string):
        return True
    if fst_string[fst_index] != sec_string[sec_index]:
        return False
    if(fst_index < len(fst_string) and sec_index < len(sec_string)):
        return is_anagram_recursive(
          fst_string, sec_string, fst_index + 1, sec_index + 1
          )
    return True
