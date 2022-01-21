def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        if type(target_time) != int:
            return None 
        count = 0
        for first, second in permanence_period:
            for i in range(first, second+1):
                if i == target_time:
                    count += 1
    
        return count
    except:
        return None
