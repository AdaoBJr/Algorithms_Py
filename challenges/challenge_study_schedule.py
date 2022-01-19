def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    result = 0

    if bool(target_time) is False:
        return None

    for student in permanence_period:
        if type(student[0]) is not int or type(student[1]) is not int:
            return None
        # if(target_time in range(start, end))
        if(target_time >= student[0] and target_time <= student[1]):
            result += 1

    return result
