def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    amount = 0
    for periods in permanence_period:

        if periods is None:
            return None

        first_value = periods[0]
        second_value = periods[1]

        if first_value is None or second_value is None:
            return None

        if first_value <= target_time and second_value >= target_time:
            amount += 1
    return amount
