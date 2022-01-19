# sort --> log n
# for i in range --> n
# complexidade n log n


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    nums.sort()
    for i in range(len(nums) - 1):
        if type(nums[i]) != int or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
