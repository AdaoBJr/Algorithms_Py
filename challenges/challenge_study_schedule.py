def study_schedule(permanence_period, target_time):
    # testabto se o target_time é int
    if type(target_time) is not int:
        return None

    count = 0
    for item in permanence_period:
        # testabto se os valores do periodo são int
        if type(item[0]) is not int or type(item[1]) is not int:
            return None
        # testabto se o valor está dentro do range
        if item[0] <= target_time and item[1] >= target_time:
            count = count + 1
    return count
