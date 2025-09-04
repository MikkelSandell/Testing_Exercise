# Picture framing price calculator
def calculate_framing_price(width_cm, height_cm):
	"""
	Calculate the price of picture framing based on width and height in cm.
	Width: 30-100 cm inclusive
	Height: 30-60 cm inclusive
	Area = width * height
	If area > 1600 cm2: price = 3500 kr
	Else: price = 3000 kr
	"""
	if not (30 <= width_cm <= 100):
		raise ValueError("Width must be between 30 and 100 cm inclusive.")
	if not (30 <= height_cm <= 60):
		raise ValueError("Height must be between 30 and 60 cm inclusive.")
	area = width_cm * height_cm
	if area > 1600:
		return 3500
	else:
		return 3000
