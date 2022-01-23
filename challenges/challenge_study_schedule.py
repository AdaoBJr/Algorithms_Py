def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    quantityStudents = 0
    if target_time is None:
        return None
    for entrada, saida in permanence_period:
        if entrada is None or saida is None:
            return None
        if entrada <= target_time <= saida:
            quantityStudents += 1
    return quantityStudents
    # Na função o parãmentro permanence-period vão as tuplas do range
    # de horarios e no target_time o horario a se testar a
    # quantidade de alunos
