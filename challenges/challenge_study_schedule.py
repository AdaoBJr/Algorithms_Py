def study_schedule(permanence_period, target_time):
    if target_time is not None:
        students = 0
        for period in permanence_period:
            if type(period[0]) != int or type(period[1]) != int:
                return None
            if target_time in range(period[0], period[1] + 1):
                students += 1
        return students
    return None
