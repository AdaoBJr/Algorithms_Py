# https://blog.betrybe.com/tecnologia/tuplas-em-python/
def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    total = 0
    for pp in permanence_period:

        if type(pp[0]) is not int or type(pp[1]) is not int:
            return None
# https://www.devmedia.com.br/estruturas-de-condicao-em-python/37158
        if pp[0] <= target_time and pp[1] >= target_time:
            total = total + 1
    return total
