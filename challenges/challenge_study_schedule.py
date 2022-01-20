def study_schedule(permanence_period, target_time):
    result = 0
    if not isinstance(target_time, int):
        return None

    for time in permanence_period:
        if not isinstance(time[0], int) or not isinstance(time[1], int):
            return None
        if time[0] <= target_time and time[1] >= target_time:
            result += 1

    return result
