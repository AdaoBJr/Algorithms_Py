# iniciando o projeto
def study_schedule(permanence_period, target_time):
    qty_students = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                qty_students += 1
        return qty_students
    except TypeError:
        return None
