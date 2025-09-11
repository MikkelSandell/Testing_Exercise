import pytest
from app.Airline_discount_policy import calculate_discount

def test_children_under_2_travel_free():
	# Rule: Children 2 and under travel for free
	assert calculate_discount(2, 'India', 'Wednesday', 1) == 1.0
	assert calculate_discount(1, 'USA', 'Monday', 10) == 1.0

def test_children_3_to_17_discount():
	# Rule: Passengers older than 2 but younger than 18 years are offered a discount of 40% for all destinations
	assert calculate_discount(3, 'India', 'Monday', 1) == 0.4
	assert calculate_discount(17, 'USA', 'Friday', 7) == 0.4

def test_adult_india_discount():
	# Rule: Passengers older than 18 with destinations in India are offered a discount of 20%, as long as the departure is not on a Monday or Friday
	assert calculate_discount(18, 'India', 'Tuesday', 1) == 0.2
	assert calculate_discount(30, 'India', 'Monday', 1) == 0.0
	assert calculate_discount(30, 'India', 'Friday', 1) == 0.0

def test_adult_non_india_discount():
	# Rule: For destinations outside of India, passengers are offered a discount of 25%, if the departure is not on a Monday or Friday
	assert calculate_discount(18, 'USA', 'Thursday', 1) == 0.25
	assert calculate_discount(40, 'France', 'Monday', 1) == 0.0
	assert calculate_discount(40, 'France', 'Friday', 1) == 0.0

def test_boundary_values_age():
	# Age = 2 (free)
		assert calculate_discount(2, 'India', 'Wednesday', 1) == pytest.approx(1.0)
		# Age = 3 (child discount)
		assert calculate_discount(3, 'India', 'Wednesday', 1) == pytest.approx(0.4)
		# Age = 17 (child discount)
		assert calculate_discount(17, 'India', 'Wednesday', 1) == pytest.approx(0.4)
		# Age = 18 (adult)
		assert calculate_discount(18, 'India', 'Wednesday', 1) == pytest.approx(0.2)
		# Age = 100 (adult)
		assert calculate_discount(100, 'India', 'Wednesday', 1) == pytest.approx(0.2)

def test_boundary_values_stay_duration():
	# Stay = 5 (no extra discount)
		assert calculate_discount(18, 'India', 'Wednesday', 5) == pytest.approx(0.2)
		# Stay = 6 (extra discount)
		assert calculate_discount(18, 'India', 'Wednesday', 6) == pytest.approx(0.3)
		# Stay = 7 (extra discount)
		assert calculate_discount(18, 'India', 'Wednesday', 7) == pytest.approx(0.3)

def test_departure_day_edge_cases():
	# Monday (no base discount for adults)
	assert calculate_discount(18, 'India', 'Monday', 1) == 0.0
	# Friday (no base discount for adults)
	assert calculate_discount(18, 'India', 'Friday', 1) == 0.0
	# Monday with long stay (only extra discount)
	assert calculate_discount(18, 'India', 'Monday', 6) == 0.1

def test_destination_case_sensitivity():
	# 'India' in different cases
	assert calculate_discount(18, 'India', 'Wednesday', 1) == 0.2
	assert calculate_discount(18, 'india', 'Wednesday', 1) == 0.2
	assert calculate_discount(18, 'INDIA', 'Wednesday', 1) == 0.2
def test_stay_duration_additional_discount():
	# Rule: Passengers who stay at least 6 days at their destination receive an additional discount of 10%
	# India, not Monday/Friday
	assert calculate_discount(18, 'India', 'Tuesday', 6) == pytest.approx(0.3)  # 0.2 + 0.1
	# Non-India, not Monday/Friday
	assert calculate_discount(18, 'USA', 'Thursday', 7) == 0.35  # 0.25 + 0.1
	# India, Monday (no base discount, but still check additional)
	assert calculate_discount(18, 'India', 'Monday', 6) == 0.1
	# Non-India, Friday (no base discount, but still check additional)
	assert calculate_discount(18, 'USA', 'Friday', 6) == 0.1
