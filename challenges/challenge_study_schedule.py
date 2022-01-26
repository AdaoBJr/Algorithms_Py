def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    number_of_students = 0
    if target_time is None:
        return None
    for period in permanence_period:
        if None in period:
            return None
        if period[0] <= target_time <= period[1]:
            number_of_students +=1
    return number_of_students
