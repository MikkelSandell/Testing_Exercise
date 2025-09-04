import pytest
from app.Password_field import PasswordField

# Equivalence partitions:
# - Invalid: <6 chars, >10 chars, non-string
# - Valid: 6-10 chars (inclusive)

def test_password_too_short():
	with pytest.raises(ValueError):
		PasswordField("abc")  # 3 chars

def test_password_too_long():
	with pytest.raises(ValueError):
		PasswordField("abcdefghijk")  # 11 chars

def test_password_non_string():
	with pytest.raises(TypeError):
		PasswordField(123456)

def test_password_valid_min():
	pf = PasswordField("abcdef")  # 6 chars
	assert pf.get_password() == "abcdef"

def test_password_valid_max():
	pf = PasswordField("abcdefghij")  # 10 chars
	assert pf.get_password() == "abcdefghij"

def test_password_valid_middle():
	pf = PasswordField("abcd1234")  # 8 chars
	assert pf.get_password() == "abcd1234"

# 3-boundary value approach (min-1, min, min+1, max-1, max, max+1)
@pytest.mark.parametrize("password,should_raise", [
	("abcde", True),      # 5 chars (min-1)
	("abcdef", False),    # 6 chars (min)
	("abcdefg", False),   # 7 chars (min+1)
	("abcdefghi", False), # 9 chars (max-1)
	("abcdefghij", False),# 10 chars (max)
	("abcdefghijk", True) # 11 chars (max+1)
])
def test_password_boundaries(password, should_raise):
	if should_raise:
		with pytest.raises(ValueError):
			PasswordField(password)
	else:
		pf = PasswordField(password)
		assert pf.get_password() == password

# Final list of test case values (summary)
@pytest.mark.parametrize("password,expected", [
	("abcdef", True),
	("abcdefg", True),
	("abcdefgh", True),
	("abcdefghi", True),
	("abcdefghij", True),
	("abcde", False),
	("abcdefghijk", False),
	("", False),
	(None, False),
	(123456, False)
])
def test_password_final_cases(password, expected):
	if expected:
		pf = PasswordField(password)
		assert pf.get_password() == password
	else:
		with pytest.raises((ValueError, TypeError)):
			PasswordField(password)
