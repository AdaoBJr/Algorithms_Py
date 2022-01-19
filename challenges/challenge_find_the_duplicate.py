def find_duplicate(nums):
    """ Faça o código aq. """
    if(len(nums) == 1):
        return False

    mylist = list(set(nums))
    for num in mylist:
        if(type(num) == str or num < 0):
            return False
        if(nums.count(num) > 1):
            return num
    return False
