def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0
    if target_time is None:
        return None

    for hours in permanence_period:
        if None in hours:
            return None

        if target_time in range(hours[0], hours[1] + 1):
            count += 1

    return count
