def study_schedule(permanence_period, target_time):
    people_present = 0

    if target_time is None:
        return None

    for (enter_time, exit_time) in permanence_period:
        if type(enter_time) is not int or type(exit_time) is not int:
            return None

        if enter_time <= target_time <= exit_time:
            people_present += 1

    return people_present
