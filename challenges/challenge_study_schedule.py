def study_schedule(permanence_period, target_time):
    contador = 0
    if not isinstance(target_time, int):
        return None
        # isinstance retorna true se for um número inteiro, nesse caso
        # verifica se deu falso 
        # https://www.w3schools.com/python/ref_func_isinstance.asp
    for people in permanence_period:
        if not isinstance(people[0], int) or not isinstance(people[1], int):
            return None
        if people[0] <= target_time and people[1] >= target_time:
            # verifica se o estudante estava nesse periodo
            contador += 1
    return contador
# https://pt.stackoverflow.com/questions/176525/como-posso-saber-se-a-vari%C3%A1vel-%C3%A9-um-n%C3%BAmero-inteiro-em-python
# Agradeço ao pedro henrique e o Lukas pela ajuda
