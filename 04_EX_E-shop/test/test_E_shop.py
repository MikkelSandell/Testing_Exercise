# Unit tests for E-shop discount calculation
import pytest
from app.E_shop import *

@pytest.mark.parametrize("amount, expected_discount, expected_final_price", [
	(299.99, 0.0, 299.99),      # Just below first boundary
	(300.00, 0.0, 300.00),      # At first boundary
	(300.01, 5.0, 285.01),      # Just above first boundary
	(799.99, 5.0, 759.99),      # Just below second boundary
	(800.00, 5.0, 760.00),      # At second boundary
	(800.01, 10.0, 720.01),     # Just above second boundary
])
def test_calculate_final_price(amount, expected_discount, expected_final_price):
	final_price, discount = calculate_final_price(amount)
	assert discount == expected_discount
	assert final_price == expected_final_price

#negative test
@pytest.mark.parametrize("func, value", [
	(calculate_discount, -100),
	(calculate_final_price, -50),
])
def test_negative_amount_raises_value_error(func, value):
	with pytest.raises(ValueError, match="Amount cannot be negative"):
		func(value)

#0 test
def test_calculate_final_price_zero():
	final_price, discount = calculate_final_price(0)
	assert discount == 0.0
	assert final_price == 0.0