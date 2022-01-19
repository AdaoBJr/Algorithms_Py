permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def study_schedule(permanence_period, target_time):
  # target_time in range(student[0], student[1]))
	result = 0

	for student in permanence_period:
			if(target_time >= student[0] and target_time <= student[1]):
				result += 1

	return result







print(study_schedule(permanence_period, 2))