def study_schedule(permanence_period, target_time):
    conter = 0

    try:
        target = int(target_time)
        for tupla_period in permanence_period:
            if int(tupla_period[0]) <= target <= int(tupla_period[1]):
                conter += 1
    except TypeError:
        return None

    return conter
