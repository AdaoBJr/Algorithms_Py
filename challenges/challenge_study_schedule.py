def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    for (start, end) in permanence_period:
        if type(start) != int or type(end) != int:
            return None
