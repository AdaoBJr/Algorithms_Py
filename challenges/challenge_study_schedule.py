def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) is not int:
        return None
    for (entrada, saida) in permanence_period:
        if type(entrada) is not int or type(saida) is not int:
            return None
        if entrada <= target_time and saida >= target_time:
            count += 1
    return count