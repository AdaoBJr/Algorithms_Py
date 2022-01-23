def study_schedule(permanence_period, target_time):
    total_students = 0
    for (x, y) in permanence_period:
        if type(x) != int or type(y) != int or target_time is None:
            return None
        if x <= target_time <= y:
            total_students += 1
    return total_students
