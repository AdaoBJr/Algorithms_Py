def find_duplicate(nums):
    nums.sort()
    for index in range(len(nums) - 1):
        if (
            not nums
            or type(nums[index]) != int
            or len(nums) < 2
            or nums[index] < 0
        ):
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False
