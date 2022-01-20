# Source https://www.horadecodar.com.br/2020/08/06/como-contar-
# o-numero-de-ocorrencias-em-uma-list-em-python/

def find_duplicate(nums):
    size = len(nums)
    if size == 1 or (size == 2 and nums[0] != nums[1]):
        return False

    for n in nums:
        if type(n) is str or n < 0:
            return False
        if nums.count(n) > 1:
            return n
