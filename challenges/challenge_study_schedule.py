def study_schedule(permanence_period, target_time):
    totalRightTime = 0

    if target_time is None:
        return None

    for entryTime, departureTime in permanence_period:
        if entryTime is None or departureTime is None:
            return None
        if entryTime <= target_time <= departureTime:
            totalRightTime += 1

    return totalRightTime
