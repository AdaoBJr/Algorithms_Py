def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None
    acc = 0
    for per in permanence_period:
        if per[0] == target_time or per[1] == target_time:
            acc += 1
            print(acc, per)
    return acc
