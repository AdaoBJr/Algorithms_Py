def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter_students = 0
    for entry_time, exit_time in permanence_period:
        if None in (entry_time, exit_time):
            return None
        if entry_time <= target_time <= exit_time:
            counter_students += 1
    return counter_students
