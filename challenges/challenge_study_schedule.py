def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students_number = 0
    if type(target_time) != int:
        return None
    for tuple in permanence_period:
        if type(tuple[0]) != int or type(tuple[1]) != int:
            return None
        if tuple[0] <= target_time <= tuple[1]:
            students_number += 1
    return students_number
