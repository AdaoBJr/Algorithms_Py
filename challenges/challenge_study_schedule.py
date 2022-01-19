def study_schedule(permanence_period, target_time):
    if target_time == 0 or type(target_time) != int:
        return None
    else:
        all_permanence = []
        # fazendo o desempacotamento de tuplas, fonte:
        # https://pythonhelp.wordpress.com/2013/01/10/desempacotamento-de-tupla/
        for entrada, saida in permanence_period:
            if type(entrada) != int or type(saida) != int:
                return None
            all_permanence.extend(range(entrada, saida + 1))

        return all_permanence.count(target_time)
