def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0
    if not target_time:
        return None
    for in_out in permanence_period:
        if not in_out[0] or in_out[1]:
            return None
    return count
