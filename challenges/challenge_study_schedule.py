def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    cont = 0

    for tupla in permanence_period:
        if type(tupla[0]) != int or type(tupla[1]) != int:
            return None
        if tupla[0] <= target_time and tupla[1] >= target_time:
            cont += 1
    return cont


# def study_schedule(permanence_period, target_time):
#     if type(target_time) != int:
#         return None
#     time = [0, 1, 2, 3, 4, 5]
#     timeCont = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

#     for tupla in permanence_period:
#         if type(tupla[0]) != int or type(tupla[1]) != int:
#             return None
#         for n in time[tupla[0]:tupla[1] + 1]:
#             timeCont[n] += 1
#     return timeCont[target_time]
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, 4))