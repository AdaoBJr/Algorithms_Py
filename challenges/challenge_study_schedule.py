def study_schedule(permanence_period, target_time):
    counter = 0
    position = 0

    while position < len(permanence_period):
        start = permanence_period[position][0]
        end = permanence_period[position][1]
        try:
            if start <= target_time <= end:
                counter += 1
            position += 1
        except TypeError:
            return None
    return counter
