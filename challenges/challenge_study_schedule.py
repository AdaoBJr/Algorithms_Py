

def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        x = 0
        for t in permanence_period:
            c = t[0] <= target_time and t[1] >= target_time

            if c is True:
                x += 1
        return x

    except TypeError:
        return None


study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2)
