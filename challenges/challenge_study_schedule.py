# Gleyson explicou sobre a descontrução dentro do for 
def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for (entrance, exit) in permanence_period:
        if entrance is None or exit is None:
            return None
        if entrance <= target_time <= exit:
            count += 1
    return count
