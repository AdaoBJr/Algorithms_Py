def study_schedule(permanence_period, target_time):
    students = list()
    if type(target_time) != int:
        return None
    for value in permanence_period:
        if type(value[0]) != int or type(value[1]) != int:
            return None
        if value[0] <= target_time <= value[1]:
            students.append(value)
    return len(students)
