def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if type(target_time) != int:
        return None
    count = 0
    for a, b in permanence_period:
        if type(a) != int or type(b) != int:
            return None
        if target_time >= a and target_time <= b:
            count += 1
    return count
