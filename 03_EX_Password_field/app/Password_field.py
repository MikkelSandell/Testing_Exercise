class PasswordField:
	def __init__(self, password: str):
		if not isinstance(password, str):
			raise TypeError("Password must be a string.")
		if len(password) < 6:
			raise ValueError("Password must be at least 6 characters long.")
		if len(password) > 10:
			raise ValueError("Password must be at most 10 characters long.")
		self.password = password

	def get_password(self):
		return self.password
