def study_schedule(permanence_period, target_time):
    students = 0
    for input, output in permanence_period:
        if None in (input, output, target_time):
            return None
        if input <= target_time <= output:
            students += 1
    return students
