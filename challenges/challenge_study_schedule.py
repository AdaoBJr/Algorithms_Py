def study_schedule(permanence_period, target_time):
    if target_time == 0 or type(target_time) != int:
        return None
    else:
        count = 0
        # fazendo o desempacotamento de tuplas, fonte:
        # https://pythonhelp.wordpress.com/2013/01/10/desempacotamento-de-tupla/
        for entrada, saida in permanence_period:
            if type(entrada) != int or type(saida) != int:
                return None
            # Feito ajuda de Gabriel Essênio
            if entrada <= target_time and saida >= target_time:
                count += 1

        return count
