def study_schedule(permanence_period, target_time):
    time = [0, 1, 2, 3, 4, 5]
    timeCont = {}
    print(permanence_period, target_time)
    for n in time:
        timeCont[n] = 0

    for tupla in permanence_period:
        # print(time [tupla[0]:tupla[1] +1])
        for n in time [tupla[0]:tupla[1] +1]:
            timeCont[n] += 1

    return timeCont[target_time]



permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_period, 4), "final")