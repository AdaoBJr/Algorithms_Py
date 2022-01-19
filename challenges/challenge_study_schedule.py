def study_schedule(permanence_period, target_time):
    if len(permanence_period) == 0:
        return 0

    period = permanence_period[0]
    if period[0] < target_time and period[0][1] > target_time:
        return study_schedule(permanence_period[1:], target_time)
