def study_schedule(permanence_period, target_time):
    if (
        target_time == '' or
        type(target_time) != int
    ):
        return None

    count = 0
    for schedule in permanence_period:
        if type(schedule[0]) != int or type(schedule[1]) != int:
            return None
        if schedule[0] <= target_time <= schedule[1]:
            count += 1

    return count


if __name__ == '__main__':
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(permanence_period, 1))
