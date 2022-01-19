def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""

    if type(target_time) is not int:
        return None
    count = 0

    for period in permanence_period:
        if not all(period):
            return None
        if target_time >= period[0] and target_time <= period[1]:
            count += 1
    return count
