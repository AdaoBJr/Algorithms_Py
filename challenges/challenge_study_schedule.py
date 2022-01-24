def study_schedule(permanence_period, target_time):
    result = 0
    for start, end in permanence_period:
        if start is None or end is None or target_time is None:
            return None
        if start <= target_time <= end:
            result += 1
    return result
