def check_permance_numbers(permanence_period):
    if len(permanence_period) > 0:
        for permance in permanence_period:
            return bool(isinstance(permance[0] and permance[1], int))

def valid_target_time(target_time):
    valid_type = isinstance(target_time, int)
    return valid_type
    

# https://www.geeksforgeeks.org/count-the-number-of-intervals-in-which-a-given-value-lies/
# https://stackoverflow.com/questions/61106572/how-to-check-if-list-only-contains-numbers
# https://pynative.com/python-isinstance-explained-with-examples/#h-isinstance-with-python-list
def study_schedule(permanence_period, target_time):
    best_time_to_post = 0


    if check_permance_numbers(permanence_period) and valid_target_time(target_time):
        for i in permanence_period:
            entrance = i[0]
            exit = i[1]
            if target_time <= exit and target_time >= entrance:
                best_time_to_post += 1
        return best_time_to_post
    else:
        return None

# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))