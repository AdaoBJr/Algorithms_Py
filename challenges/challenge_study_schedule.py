def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    total_students = 0
    for system_login, system_logout in permanence_period:
        if None in (system_login, system_logout):
            return None
        if system_login <= target_time <= system_logout:
            total_students += 1
    return total_students
