def study_schedule(permanence_period, target_time):
    count = 0
    for pp in permanence_period:
        if (
            not isinstance(pp[0], int)
            or not isinstance(pp[1], int)
            or not isinstance(target_time, int)
        ):
            pass
        elif pp[0] <= target_time and pp[1] >= target_time:
            count += 1

    if count == 0:
        return None
    else:
        return count
    # if len(permanence_period) == 0:
    #     return None

    # period = permanence_period[0]

    # if not isinstance(period[0], int) or not isinstance(period[1], int):
    #     return study_schedule(permanence_period[1:], target_time)
    # elif period[0] <= target_time and period[1] >= target_time:
    #     return 1 + study_schedule(permanence_period[1:], target_time)
    # else:
    #     return study_schedule(permanence_period[1:], target_time)
