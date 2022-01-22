def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students_present = 0
    for student_permanence_hours in permanence_period:
        if (
            type(student_permanence_hours[0]) is not int
            or type(student_permanence_hours[1]) is not int
        ):
            return None
        if (
            student_permanence_hours[0]
            <= target_time
            <= student_permanence_hours[1]
        ):
            students_present += 1

    return students_present
