def study_schedule(permanence_period, target_time):
    position = len(permanence_period) // 2 - 1

    if target_time and permanence_period[position][1]:
        if target_time >= permanence_period[position][1]:
            newList = permanence_period[(position):]
        else:
            newList = permanence_period[: (position + 2)]

        return verifyInter(newList, target_time)

    else:
        return None


def verifyInter(list, target):
    count = 0
    for item in list:
        if item[0] or item[1]:
            if item[0] <= target <= item[1]:
                count += 1
        else:
            return None

    return count
