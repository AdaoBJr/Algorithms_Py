def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if(type(target_time) != int):
        return None
    count = 0;
    
    for peooples in permanence_period:
        if type(peooples) is not int:
            return None
    return count