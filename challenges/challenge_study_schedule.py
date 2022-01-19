def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    x = 0
    for time in permanence_period:
        type1 = type(time[0]) is not int
        type2 = type(time[1]) is not int
        if type1 or type2 or target_time is None:
            return None

        equal = time[0] == target_time or time[1] == target_time
        bigger_or_less = time[0] <= target_time and time[1] >= target_time

        if bigger_or_less is True or equal is True:
            x += 1

    if x == 0:
        return None
    return x


study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2)
