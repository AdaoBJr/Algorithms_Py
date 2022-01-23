def study_schedule(permanence_period, target_time):
    try:
        time_validation = [
            tupla
            for tupla in permanence_period
            if tupla[0] <= target_time <= tupla[1]
        ]
        if time_validation != []:
            counter = len(time_validation)
    except TypeError:
        return None
    return counter
