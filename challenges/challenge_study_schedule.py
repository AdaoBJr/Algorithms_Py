from asyncio.windows_events import NULL


def study_schedule(permanence_period, target_time):
    students_by_period = {}
    if target_time == None:
        return None

    for tupla in permanence_period:
        if type(tupla[0]) != int or type(tupla[1]) != int:
            return None
        for i in range(tupla[0], tupla[1] + 1):
            if i in students_by_period:
                students_by_period[i] += 1
            else:
                students_by_period[i] = 1

    return students_by_period[target_time]

print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], None))