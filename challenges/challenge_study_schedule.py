def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    for time_record in permanence_period:
        if None in time_record or target_time is None:
            return None
        if time_record[0] <= target_time and time_record[1] >= target_time:
            counter += 1
    return counter
