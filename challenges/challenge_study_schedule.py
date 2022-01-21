def study_schedule(permanence_period, target_time):
    online_student = 0

    if target_time is None:
        return None

    for (inicio, fim) in permanence_period:
        if type(inicio) != int or type(fim) != int:
            return None
        if inicio <= target_time <= fim:
            online_student += 1
    return online_student
