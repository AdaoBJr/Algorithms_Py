from tokenize import Number


def study_schedule(permanence_period, target_time):
    if target_time == '':
        return None

    a = target_time
    for time in permanence_period: 
       if (type(time[0]) and type(time[1])) !=  int:
           return None

study_schedule([(1, 5), (2, 4), (3, 3), (4, 4), (5, 5)], 3)