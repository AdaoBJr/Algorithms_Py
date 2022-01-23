def study_schedule(permanence_period, target_time):
    try:
        left_pointer = 0
        right_pointer = len(permanence_period) - 1
        all_period = []

        while left_pointer <= right_pointer:
            period = permanence_period[left_pointer]
            if period[1] - period[0] != 0:
                all_period.extend(range(period[0], period[1] + 1))
            else:
                all_period.append(period[0])

            left_pointer += 1

            count = all_period.count(target_time)

        # https://pt.stackoverflow.com/questions/161505/em-python-existe-opera%C3%A7%C3%A3o-tern%C3%A1ria
        return count if count != 0 else None

        # return all_period.count(target_time)
    except TypeError:
        return None
