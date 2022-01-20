def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) != int:
        return None
    for (entrada, saida) in permanence_period:
        if type(entrada) != int or type(saida) != int:
            return None
        if entrada <= target_time and saida >= target_time:
            count += 1
    return count