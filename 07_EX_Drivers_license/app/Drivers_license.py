# Decision logic for driver's license evaluation
def evaluate_candidate(theory, practical):
	# Handle invalid values
	if theory < 0 or practical < 0:
		return {
			"license_granted": False,
			"repeat_theory": theory < 85,
			"repeat_practical": False,
			"extra_lessons": False
		}
	# License granted if theory >= 85 and practical <= 2
	license_granted = theory >= 85 and practical <= 2
	repeat_theory = theory < 85
	repeat_practical = practical > 2
	extra_lessons = repeat_theory and repeat_practical
	# Edge case: theory > 100 is still considered passing
	if theory > 100:
		license_granted = True
		repeat_theory = False
	return {
		"license_granted": license_granted,
		"repeat_theory": repeat_theory,
		"repeat_practical": repeat_practical,
		"extra_lessons": extra_lessons
	}
