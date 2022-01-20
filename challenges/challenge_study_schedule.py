def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    hour = 0
    for p in permanence_period:
        if type(p[0]) is not int or type(p[1]) is not int:
            return None

        if p[0] <= target_time <= p[1]:
            hour += 1

    return hour
