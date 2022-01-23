def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    total_students = 0
    for (entry, exit) in permanence_period:
        if not isinstance(entry, int) or not isinstance(exit, int):
            return None

        if entry <= target_time <= exit:
            total_students += 1

    return total_students
