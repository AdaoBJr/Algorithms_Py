def study_schedule(permanence_period, target_time):
    time = [0, 1, 2, 3, 4, 5, 6, 7]
    timeCont = {}
    for n in time:
        timeCont[n] = 0
    for tupla in permanence_period:
        for n in time[tupla[0]:tupla[1] + 1]:
            timeCont[n] += 1
    return timeCont[target_time]
