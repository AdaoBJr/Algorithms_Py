def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return - 1


def find_duplicate(nums):
    try:
        nums_sorted = sorted(nums)
        for index, item in enumerate(nums_sorted):
            new_array = nums_sorted.pop(index)
            if type(item) is not int:
                return False
            return binary_search_iterative(new_array, item)
    except TypeError:
        return False
