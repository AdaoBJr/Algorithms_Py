def next_stage(sorted):
    result = {"max": "0", "num": 0}
    for key, value in sorted.items():
        if value > result["num"]:
            result["num"] = value
            result["max"] = key
    if result["num"] < 2:
        return False
    return result["max"]


def find_duplicate(nums):
    if len(nums) < 1:
        return False

    repete_nums = {}
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False
        repete_nums[num] = repete_nums.get(num, 0) + 1
    return next_stage(repete_nums)
