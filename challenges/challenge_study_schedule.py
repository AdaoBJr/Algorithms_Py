def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    response = 0
    for period in permanence_period:
        if None in period:
            return None
        if period[0] <= target_time <= period[1]:
            response += 1
    return response
