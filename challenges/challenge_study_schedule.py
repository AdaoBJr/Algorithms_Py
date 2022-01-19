def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for p in permanence_period:
        if not p[0] or not p[1] or p[0] != int(p[0]) or p[1] != int(p[1]):
            return None
        if p[0] <= target_time and p[1] >= target_time:
            count += 1

    return count
