def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    try:
        for entrance, exit in permanence_period:
            if entrance <= target_time <= exit:
                counter += 1
    except TypeError:
        return None
    # if target_time is None:
    #     return None
    return counter


permanence = [(2, None), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
study_schedule(permanence, None)
