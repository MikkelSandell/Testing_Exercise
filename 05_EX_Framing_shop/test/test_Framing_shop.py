
import pytest
from app.Framing_shop import calculate_framing_price

# Valid cases: (width, height, expected_price)
@pytest.mark.parametrize("width, height, expected_price", [
	(30, 30, 3000),      # min width, min height
	(100, 60, 3500),     # max width, max height
	(30, 60, 3500),      # min width, max height
	(100, 30, 3500),     # max width, min height
	(31, 31, 3000),      # just above min
	(99, 59, 3500),      # just below max
	(40, 40, 3000),      # area exactly 1600
	(40, 41, 3500),      # area just above 1600
	(40, 39, 3000),      # area just below 1600
])
def test_calculate_framing_price_valid(width, height, expected_price):
	assert calculate_framing_price(width, height) == expected_price

# Invalid cases: (width, height, expected_exception)
@pytest.mark.parametrize("width, height", [
	(29, 40),    # width below min
	(101, 40),   # width above max
	(40, 29),    # height below min
	(40, 61),    # height above max
])
def test_calculate_framing_price_invalid(width, height):
	with pytest.raises(ValueError):
		calculate_framing_price(width, height)
