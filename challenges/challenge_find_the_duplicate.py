from unicodedata import numeric


def find_duplicate(nums):
    if nums is None or len(nums) <= 2 or isinstance(nums, str):
        return False

    for index, number in enumerate(nums):
        for indexY, numberY in enumerate(nums):
            if index != indexY and number == numberY:
                return number

    return False
