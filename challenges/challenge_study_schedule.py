def study_schedule(permanence_period, target_time):
    student = 0

    if target_time is None:
        return None

    for (inicio, fim) in permanence_period:
        if type(inicio) != int or type(fim) != int:
            return None
        if inicio <= target_time <= fim:
            student += 1
    return student

    # print(f"inicio: {inicio}, fim: {fim}")
    # if target_time in range(inicio, fim):
