from tkinter import N


def study_schedule(permanence_period, target_time):
    #Retorne None se em target_time houver alguma entrada inválida
    if(target_time is None): return None # = null

    contador = 0;
    for (entrada, saida) in permanence_period:
        if entrada is None or saida is None: return None;
        #Entrada tem que ser <= time e saida tem que ser >= time
        if (entrada <= target_time) and (saida >= target_time):
            contador += 1
    return contador;         



