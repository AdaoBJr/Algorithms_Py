def study_schedule(permanence_period, target_time):
    # Verifica se o horário passado (target_time) é um número
    if type(target_time) is not int:
        return None

    students = 0
    for permanence in permanence_period:
        # Verifica se a hora de entrada (permanence[0]) e a hora de saída (permanence[1]) são inteiros
        if type(permanence[0]) is not int or type(permanence[1]) is not int:
            return None
        # Verifica se o horário passado (target_time) está entre os horários de entrada e saída. Caso esteja, siginifica que existe pelo menos um estudante naquele horário, então ele acrescenta esse estudante à variável 'students'
        if permanence[0] <= target_time <= permanence[1]:
            students = students + 1
    return students
