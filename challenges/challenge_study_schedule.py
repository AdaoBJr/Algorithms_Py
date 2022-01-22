def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    count = 0
    for (entrance, exit) in permanence_period:
        if not entrance:
            return None
        if not exit:
            return None
        if entrance <= target_time <= exit:
            count += 1
    return count