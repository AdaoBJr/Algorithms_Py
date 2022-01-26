def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) <= 1:
        return False

    for num in nums:
        if type(num) != int or num < 0:
            return False
        repeated_list = [num for num in nums if nums.count(num) > 1]
        if len(repeated_list) > 0:
            return repeated_list[0]
        else:
            return False
