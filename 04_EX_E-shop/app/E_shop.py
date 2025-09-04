# Payment discount calculation for e-shop
def calculate_discount(amount_kr):
	"""
	Calculate the discount percentage based on the purchase amount.
	:param amount_kr: float, purchase amount in kroner (accuracy 0.01)
	:return: float, discount percentage (0, 5, or 10)
	"""
	if amount_kr < 0:
		raise ValueError("Amount cannot be negative")
	if amount_kr <= 300:
		return 0.0
	elif amount_kr <= 800:
		return 5.0
	else:
		return 10.0

def calculate_final_price(amount_kr):
	"""
	Calculate the final price after applying the discount.
	:param amount_kr: float, purchase amount in kroner (accuracy 0.01)
	:return: tuple (final_price, discount_percent)
	"""
	if amount_kr < 0:
		raise ValueError("Amount cannot be negative")
	discount_percent = calculate_discount(amount_kr)
	discount_amount = amount_kr * (discount_percent / 100)
	final_price = round(amount_kr - discount_amount, 2)
	return final_price, discount_percent
