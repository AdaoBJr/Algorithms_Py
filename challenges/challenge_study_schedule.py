def study_schedule(permanence_period, target_time):
    people_studying = 0

    if target_time is None:
        return None

    for (start_study, finish_study) in permanence_period:
        if type(start_study) is not int or type(finish_study) is not int:
            return None

        if start_study <= target_time <= finish_study:
            people_studying += 1

    return people_studying


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
