def study_schedule(permanence_period, target_time):
    count = 0
    if (not target_time):
        return None
    for peooples in permanence_period:
        if (type(peooples[0]) != int):
            return None
        if (peooples[0] <= target_time <= peooples[1]):
            count += 1
    return count
