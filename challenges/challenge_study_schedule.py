def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter_students = 0
    for time  in permanence_period:
        if None in (time[0], time[1]):
            return None
        if time[0] <= target_time <= time[1]:
            counter_students += 1
    return counter_students
