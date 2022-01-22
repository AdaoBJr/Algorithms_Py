def study_schedule(permanence_period, target_time):
    if target_time == None:
        return

    count = 0

    for i in permanence_period:
        if type(i[0]) == int and type(i[1]) == int:
            if i[0] <= target_time and i[1] >= target_time:
                count += 1
        else:
            return
    return count
