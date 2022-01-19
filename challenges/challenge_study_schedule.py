def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    count = 0

    for period in permanence_period:
        if not type(period[0]) == int or not type(period[1]) == int:
            return None
        if target_time >= period[0] and target_time <= period[1]:
            count += 1
    return count
