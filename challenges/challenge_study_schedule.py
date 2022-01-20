def study_schedule(permanence_period, target_time):
    students_online = 0
    if type(permanence_period) != list or type(target_time) != int:
        return None
    else:
        for item in permanence_period:
            if item[0] is None or item[1] is None:
                return None
            elif target_time >= item[0] and target_time <= item[1]:
                students_online += 1
        return students_online
