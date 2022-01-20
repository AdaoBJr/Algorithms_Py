def find_duplicate(nums):
    """ Faça o código aqui. """
    result = []
    if len(nums) <= 1:
        return False
    else:
        for num in nums:
            if (
                isinstance(num, str) or num < 0
            ):  # se o num for string ou se for negativo*
                return False
            result = set(
                [num for num in nums if nums.count(num) > 1]
            )  # coloca os numeros repetidos em um set **
            print(result)
            if len(result) > 0:  # se tiver numeros repetidos
                return result.pop()  # retorna o numero repetido, fora do set
            else:
                return False


# *https://www.w3schools.com/python/ref_func_isinstance.asp
# **https://www.delftstack.com/pt/howto/python/python-find-duplicates-in-list/

# nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# print(find_duplicate(nums))
