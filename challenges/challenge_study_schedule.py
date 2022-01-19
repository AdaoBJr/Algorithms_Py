def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    result = 0
    if target_time is None:
        return None
    for entrada, saida in permanence_period:
        if entrada is None or saida is None:
            return None
        if entrada <= target_time <= saida:
            result += 1
    return result
