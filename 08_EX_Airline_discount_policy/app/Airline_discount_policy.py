from datetime import datetime

def calculate_discount(age, destination, departure_day, stay_duration):
	"""
	Calculate the discount for a passenger based on age, destination, departure day, and stay duration.
    
	Parameters:
		age (int): Age of the passenger
		destination (str): Destination country
		departure_day (str): Day of the week (e.g., 'Monday')
		stay_duration (int): Number of days at destination
	Returns:
		float: Discount percentage (0.0 to 1.0)
	"""
	# Children 2 and under travel for free
	if age <= 2:
		return 1.0
	# Passengers older than 2 but younger than 18 years: 40% discount for all destinations
	if 2 < age < 18:
		return 0.4
	# Passengers 18 and older
	discount = 0.0
	if departure_day not in ['Monday', 'Friday']:
		if destination.lower() == 'india':
			discount = 0.2
		else:
			discount = 0.25
	# Additional 10% discount for stays of at least 6 days
	if stay_duration >= 6:
		discount += 0.1
	return discount
