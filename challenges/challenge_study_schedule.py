def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time:
        return None
    for (beginning, end) in permanence_period:
        if type(beginning) != int or type(end) != int:
            return None
        if beginning <= target_time <= end:
            counter += 1
    # print(counter)
    return counter


study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5)
