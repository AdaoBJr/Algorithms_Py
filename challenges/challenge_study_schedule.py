def study_schedule(permanence_period, target_time):
    left_pointer = 0
    right_pointer = len(permanence_period) - 1
    all_period = []
    start_period = permanence_period[left_pointer][0]
    exit_period = permanence_period[left_pointer][1]

    if type(target_time) != int or target_time is None:
        return None

    if type(start_period) != int or type(exit_period) != int:
        return None

    if start_period is None or exit_period is None:
        return None

    while left_pointer <= right_pointer:
        period = permanence_period[left_pointer]
        # exit_period = permanence_period[left_pointer][1]
        difference = period[1] - period[0]
        """ if type(period[0]) != int or type(period[1]) != int:
            return None
        elif period[0] is None or period[1] is None:
            return None """
        if difference != 0:
            all_period.extend(range(period[0], period[1] + 1))
            # exit_period -= 1
            left_pointer += 1
        else:
            all_period.append(period[0])
            left_pointer += 1
    return all_period.count(target_time)
