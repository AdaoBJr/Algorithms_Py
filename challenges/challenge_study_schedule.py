def study_schedule(permanence_period, target_time):
    result = 0
    if type(target_time) is not int:
        return None

    for time in permanence_period:
        if type(time[0]) is not int or type(time[1]) is not int:
            return None
        if time[0] <= target_time and time[1] >= target_time:
            result += 1

    return result
