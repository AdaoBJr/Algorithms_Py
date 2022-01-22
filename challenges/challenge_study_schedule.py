def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    amount = 0
    for student_permanence_hours in permanence_period:
        checkIn, CheckOut = (
            student_permanence_hours[0],
            student_permanence_hours[1],
        )
        if type(checkIn) is not int or type(CheckOut) is not int:
            return None
        if checkIn <= target_time <= CheckOut:
            amount += 1

    return amount
