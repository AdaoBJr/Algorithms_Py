def study_schedule(permanence_period, target_time):
    students_online = 0
    if type(target_time) is not int:
        return None
    for (login, logout) in permanence_period:
        if type(login) is not int or type(logout) is not int:
            return None
        if login <= target_time <= logout:
            students_online += 1
    return students_online
