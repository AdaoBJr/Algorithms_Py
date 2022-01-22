def study_schedule(permanence_period, target_time=None):
    counter = 0
    if target_time is None:
        return None
    else:
        for (arrival_time, departure_time) in permanence_period:
            if (type(arrival_time) is not int) or (
                type(departure_time) is not int
            ):
                counter = None
                break
            elif arrival_time <= target_time <= departure_time:
                counter += 1
    return counter
