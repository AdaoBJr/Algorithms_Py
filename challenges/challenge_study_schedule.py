def study_schedule(permanence_period, target_time):
    count = 0
    i = 0
    size = len(permanence_period)

    if target_time is None:
        return None

    while (i < size):
        if None in permanence_period[i]:
            return None
        elif permanence_period[i][0] <= target_time <= permanence_period[i][1]:
            count += 1            

        i += 1

    return count