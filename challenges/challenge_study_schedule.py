def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for value in permanence_period:
        if type(value[0]) != int or type(value[1]) != int:
            return None
        for index in range(value[0], value[1] + 1):
            dict[index] += 1
    return dict[target_time]
