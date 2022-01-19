def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time == None:
        return None
    count = 0
    for period in permanence_period:
        if not all(period):
            return None
        if target_time in period:
            count += 1
    return count
