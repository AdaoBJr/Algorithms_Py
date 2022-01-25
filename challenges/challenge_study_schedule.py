from asyncio.windows_events import NULL


def study_schedule(permanence_period, target_time):
    if target_time < 0 or target_time is NULL:
        return None
    occurrencies = 0
    for schedule in permanence_period:
        if schedule[0] >= target_time or schedule[1] <= target_time:
            occurrencies += 1
    return occurrencies
