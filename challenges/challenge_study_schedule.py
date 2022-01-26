#  estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

def study_schedule(permanence_period, target_time):
    result = 0

    if not target_time:
        return None
    
    for period in permanence_period:

        if None in period:
            return None

        if period[0] <= target_time <= period[1]:
            result += 1
    return result

