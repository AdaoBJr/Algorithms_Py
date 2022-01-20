def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not target_time:
        return None
    for in_out in permanence_period:
        if (in_out[0] is None) or (in_out[1] is None):
            return None

    return count_only(permanence_period, target_time)


# https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/
# Tricks é palavra pra te ajudar se um monstro em python
def count_only(permanence_period, target_time):
    count = 0
    for in_out in permanence_period:
        if in_out[0] <= target_time <= in_out[1]:
            count += 1
    return count
