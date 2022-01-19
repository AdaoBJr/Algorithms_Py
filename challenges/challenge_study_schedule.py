def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    result = 0

    if bool(target_time) is False:
        return None

    for student in permanence_period:
        start = student[0]
        end = student[1]
        if type(start) != int or type(end) != int:
            return None
        # if(target_time in range(start, end))
        if(target_time >= start and target_time <= end):
            result += 1

    return result
