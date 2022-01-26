def study_schedule(permanence_period, target_time):
    students = 0
    if type(target_time) != int:
        return None

    for (start, end) in permanence_period:
        if type(start) != int or type(end) != int:
            return None

        if start <= target_time <= end:
            students += 1

    return students
