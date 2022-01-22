def study_schedule(permanence_period, target_time):
    result = 0

    # não existe null em python, none representa null
    if target_time is None:
        return None

    for input_data, output_data in permanence_period:
        if input_data is None or output_data is None:
            return None
        if input_data <= target_time <= output_data:
            result += 1
        return result
