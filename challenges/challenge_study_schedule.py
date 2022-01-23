def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time == 0 or target_time is None:
        return None

    for schedule in permanence_period:
        if isinstance(schedule, str):
            return None
        elif schedule[0] is None or schedule[1] is None:
            return None
        elif schedule[0] <= target_time <= schedule[1]:
            counter += 1

    return counter
