def find_duplicate(nums):
    for num in nums:
        cont2 = 0
        cont = len(nums) - 1
        if not nums or type(num) != int or len(nums) < 2 or num < 0:
            return False
        for index in range(len(nums)):
            if num == nums[cont]:
                cont2 += 1
            cont -= 1
        if cont2 > 1:
            return num
    return False
