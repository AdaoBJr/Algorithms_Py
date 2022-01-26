
def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    occurrencies = 0
    for schedule in permanence_period:
        if None in schedule:
            return None
        if schedule[0] <= target_time and schedule[1] >= target_time:
            occurrencies += 1
    return occurrencies
