def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    restul = 0
    for start in permanence_period:
        if start[0] is None or start[1] is None:
            return None
        if start[0] <= target_time <= start[1]:
            restul += 1
    return restul

