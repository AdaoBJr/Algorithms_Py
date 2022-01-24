def study_schedule(permanence_period, target_time):
    counter = 0

    if target_time is None:
        return None

    for student in permanence_period:
        if student[0] is None or student[1] is None:
            return None
        if student[0] <= target_time <= student[1]:
            counter += 1

    return counter


teste = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(teste, None))
