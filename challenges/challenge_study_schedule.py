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


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 3))
