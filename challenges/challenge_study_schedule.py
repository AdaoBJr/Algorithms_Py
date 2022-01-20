def study_schedule(permanence_period, target_time):
    student = 0

    if target_time == None:
        return None

    for (inicio, fim) in permanence_period:
        # print(f"inicio: {inicio}, fim: {fim}")
        if type(inicio) != int or type(fim) != int:
            return None
        if inicio <= target_time <= fim:
            # if target_time in range(inicio, fim):
            student += 1
    return student
