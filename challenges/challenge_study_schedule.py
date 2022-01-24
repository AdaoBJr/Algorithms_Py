def study_schedule(permanence_period, target_time):
    response = 0
    if target_time is None:
        return None
    for period in permanence_period:
        if None in (period[0], period[1]):
            return None
        if period[0] <= target_time <= period[1]:
            response += 1
    return response
