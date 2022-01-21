def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0
    for a, b in permanence_period:
        if type(target_time) != int or type(a) != int or type(b) != int:
            return None
        # for i in range(a, b+1):
        #     if i == target_time:
        #         count += 1
        if target_time >= a and target_time <= b:
            count += 1
    return count
