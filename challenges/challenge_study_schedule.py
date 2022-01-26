def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None
    count = 0
    for student in permanence_period:
        if type(student[0]) is not int or type(student[1]) is not int:
            return None
        if student[0] <= target_time <= student[1]:
            count += 1
    return count
