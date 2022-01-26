"""
   Material consultado sobre checar o tipo de um objeto
   https://www.w3schools.com/python/ref_func_isinstance.asp
"""


def permanence_period_is_valid(permanence_period):
    for entry_time, departure_time in permanence_period:
        if (
            entry_time is None
            or departure_time is None
            or isinstance(entry_time, int) is False
            or isinstance(departure_time, int) is False
            or departure_time < entry_time
        ):
            return False
    return True


"""
   Material consultado sobre iteração sobre lista de tuplas
   https://code-maven.com/python-iterate-list-of-tuples

   Material consultado sobre checar se é do tipo int
   https://python-reference.readthedocs.io/en/latest/docs/float/is_integer.html
"""


def number_of_students_present(permanence_period, target_time):
    number = 0
    for entry_time, departure_time in permanence_period:
        if (
            not type(entry_time) is int
            or not type(departure_time) is int
            or departure_time < entry_time
        ):
            return None
        if entry_time <= target_time <= departure_time:
            number += 1

    return number


"""
    Material consultado sobre tipo nulo
    https://appdividend.com/2019/08/16/null-object-in-python-example-python-null-value-tutorial/
"""


def study_schedule(permanence_period, target_time):
    if (
        target_time is None
        or permanence_period is None
        # or permanence_period_is_valid(permanence_period) is False
    ):
        return None

    result = number_of_students_present(permanence_period, target_time)

    # for t_time in range(target_time, 0, -1):
    #     number = number_of_students_present(permanence_period, t_time)
    #     print(f"t_time {t_time}: {number}")
    #     if number > max_students:
    #         max_students = number

    return result


# if __name__ == "__main__":
#     permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
#     tempo = 5
#     print(f"{study_schedule(permanence_periods, tempo)}")
