def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    result = 0

    for time in permanence_period:
        if None in time:
            return None

        if (time[0] <= target_time) and (time[1] >= target_time):
            result += 1
    return result
