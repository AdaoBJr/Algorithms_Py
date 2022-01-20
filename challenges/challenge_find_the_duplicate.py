def bubble_sort(lista):
    tam = len(lista)-1
    for passnum in range(tam, 0, -1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista


def find_duplicate(nums):
    """ Faça o código aqui. """
    duplicate_num = 0
    if not nums:
        return False
    orded_nums = bubble_sort(nums)
    for i in range(0, len(orded_nums) - 1, 1):
        try:
            if orded_nums[i] < 0 or type(orded_nums[i]) == str:
                return False
            if orded_nums[i] == orded_nums[i + 1]:
                duplicate_num = orded_nums[i]
                return duplicate_num
        except TypeError:
            return False

    return False
