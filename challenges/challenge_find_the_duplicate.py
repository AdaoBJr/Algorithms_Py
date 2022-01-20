# fiz em parceria com o Pedro Henrique Pires do Nascimento
def find_duplicate(nums):
    if "" in nums or not nums or len(nums) == 1:
        return False
    if len(nums) <= 2 and nums[0] != nums[1]:
        return False
    result = finde(nums, 0, 0)

    return result


def finde(nums, count, value):
    if len(nums) == 1:
        return value
    for n in nums[1:]:
        # print(n, nums[0])
        if not isinstance(nums[0], int) or nums[0] <= 0:
            return False
        if nums[0] == n and nums[0] > value:
            count += 1
            value = n
            return finde(nums[1:], count, value)
    return finde(nums[1:], count, value)
