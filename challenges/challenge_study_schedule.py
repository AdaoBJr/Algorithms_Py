def validation(tupla):
    for ele in tupla:
        if ele is None or isinstance(ele, str):
            return False
    return True


def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time in (0, None):
        return None

    for schedule in permanence_period:
        if validation(schedule) is False:
            return None
        elif schedule[0] <= target_time <= schedule[1]:
            counter += 1

    return counter
