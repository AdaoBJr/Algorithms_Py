def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        list_best_time = [
            (in_, out)
            for in_, out in permanence_period
            if in_ <= target_time <= out
        ]

        return len(list_best_time)
    except TypeError:
        return None
