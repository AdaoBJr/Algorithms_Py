def find_duplicate(nums):
    duplicates = []
    repeat = []
    for i in nums:
        if i not in duplicates:
            duplicates.append(i)

    for j in duplicates:
        if duplicates.count(j) > 1:
            if j not in repeat:
                repeat.append(i)

    # repeat = {duplicates.count(item) for item in duplicates}

    if type(nums) != int or nums < 1:
        return False

    # print(repeat)
    return repeat
