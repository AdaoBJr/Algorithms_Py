def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    students = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None

        if (period[0] <= target_time and period[1] >= target_time):
            students += 1

    return students
