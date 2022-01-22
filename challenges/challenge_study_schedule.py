def study_schedule(permanence_period, target_time):
    count = 0
    position = len(permanence_period) // 2

    if(type(target_time) is not int or permanence_period[position] is not int):
        return None

    if(target_time < permanence_period[position]):
        newList = permanence_period[position:]
    else:
        newList = permanence_period[position:]

    for item in newList:
        #print(type(item[0]) is int)
        if(type(item[0]) is not int or type(item[1]) is not int):
            return None
        if(item[0] <= target_time <= item[1]):
            count += 1

    return count