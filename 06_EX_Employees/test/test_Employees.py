import pytest
from app.Employees import Employee
from datetime import datetime, timedelta

def valid_employee():
	return Employee(
		cpr="1234567890",
		first_name="John",
		last_name="Doe",
		department="IT",
		base_salary=50000,
		educational_level=2,
		date_of_birth="11/09/1990",
		date_of_employment="11/09/2020",
		country="Denmark"
	)

# CPR
@pytest.mark.parametrize("cpr,valid", [
	("1234567890", True),
	("123456789", False),
	("abcdefghij", False),
	("12345678901", False),
])
def test_cpr_validation(cpr, valid):
	if valid:
		emp = valid_employee()
		emp.set_cpr(cpr)
		assert emp.get_cpr() == cpr
	else:
		emp = valid_employee()
		with pytest.raises(ValueError):
			emp.set_cpr(cpr)

# First name
@pytest.mark.parametrize("first_name,valid", [
	("John", True),
	("J", True),
	("J"*31, False),
	("John-Doe", True),
	("John Doe", True),
	("John123", False),
])
def test_first_name_validation(first_name, valid):
	emp = valid_employee()
	if valid:
		emp.set_first_name(first_name)
		assert emp.get_first_name() == first_name
	else:
		with pytest.raises(ValueError):
			emp.set_first_name(first_name)

# Last name
@pytest.mark.parametrize("last_name,valid", [
	("Doe", True),
	("D", True),
	("D"*31, False),
	("Doe-Smith", True),
	("Doe Smith", True),
	("Doe123", False),
])
def test_last_name_validation(last_name, valid):
	emp = valid_employee()
	if valid:
		emp.set_last_name(last_name)
		assert emp.get_last_name() == last_name
	else:
		with pytest.raises(ValueError):
			emp.set_last_name(last_name)

# Department
@pytest.mark.parametrize("department,valid", [
	("HR", True),
	("Finance", True),
	("IT", True),
	("Sales", True),
	("General Services", True),
	("Marketing", False),
	("", False),
])
def test_department_validation(department, valid):
	emp = valid_employee()
	if valid:
		emp.set_department(department)
		assert emp.get_department() == department
	else:
		with pytest.raises(ValueError):
			emp.set_department(department)

# Base salary
@pytest.mark.parametrize("salary,valid", [
	(20000, True),
	(100000, True),
	(19999, False),
	(100001, False),
	(50000.5, True),
	("50000", False),
])
def test_base_salary_validation(salary, valid):
	emp = valid_employee()
	if valid:
		emp.set_base_salary(salary)
		assert emp.get_base_salary() == salary
	else:
		with pytest.raises(ValueError):
			emp.set_base_salary(salary)

# Educational level
@pytest.mark.parametrize("level,valid", [
	(0, True),
	(1, True),
	(2, True),
	(3, True),
	(4, False),
	(-1, False),
	("2", False),
])
def test_educational_level_validation(level, valid):
	emp = valid_employee()
	if valid:
		emp.set_educational_level(level)
		assert emp.get_educational_level() in ["none", "primary", "secondary", "tertiary"]
	else:
		with pytest.raises(ValueError):
			emp.set_educational_level(level)

# Date of birth
@pytest.mark.parametrize("dob,valid", [
	("11/09/1990", True),
	("11/09/2010", False),  # too young
	("31/02/1990", False),  # invalid date
	("1990/09/11", False),  # wrong format
])
def test_date_of_birth_validation(dob, valid):
	emp = valid_employee()
	if valid:
		emp.set_date_of_birth(dob)
		assert emp.get_date_of_birth() == dob
	else:
		with pytest.raises(ValueError):
			emp.set_date_of_birth(dob)

# Date of employment
@pytest.mark.parametrize("doe,valid", [
	("11/09/2020", True),
	("11/09/2026", False),  # future date
	("31/02/2020", False),  # invalid date
	("2020/09/11", False),  # wrong format
])
def test_date_of_employment_validation(doe, valid):
	emp = valid_employee()
	if valid:
		emp.set_date_of_employment(doe)
		assert emp.get_date_of_employment() == doe
	else:
		with pytest.raises(ValueError):
			emp.set_date_of_employment(doe)

# Country
@pytest.mark.parametrize("country,valid", [
	("Denmark", True),
	("", False),
	(None, False),
])
def test_country_validation(country, valid):
	emp = valid_employee()
	if valid:
		emp.set_country(country)
		assert emp.get_country() == country
	else:
		with pytest.raises(ValueError):
			emp.set_country(country)

# getSalary
@pytest.mark.parametrize("base_salary,educational_level,expected", [
	(20000, 0, 20000),
	(30000, 1, 31220),
	(40000, 2, 42440),
	(50000, 3, 53660),
])
def test_get_salary(base_salary, educational_level, expected):
	emp = valid_employee()
	emp.set_base_salary(base_salary)
	emp.set_educational_level(educational_level)
	assert emp.getSalary() == expected

# getDiscount
@pytest.mark.parametrize("years,expected", [
	(0, 0.0),
	(1, 0.5),
	(5, 2.5),
	(10, 5.0),
])
def test_get_discount(years, expected):
	emp = valid_employee()
	date = (datetime.now() - timedelta(days=years*365)).strftime("%d/%m/%Y")
	emp.set_date_of_employment(date)
	assert emp.getDiscount() == expected

# getShippingCosts
@pytest.mark.parametrize("country,expected", [
	("Denmark", 0),
	("Norway", 0),
	("Sweden", 0),
	("Iceland", 50),
	("Finland", 50),
	("Germany", 100),
	("USA", 100),
])
def test_get_shipping_costs(country, expected):
	emp = valid_employee()
	emp.set_country(country)
	assert emp.getShippingCosts() == expected

def test_employee_getSalary_with_mock(mocker):
    emp = Employee(
        cpr="1234567890",
        first_name="John",
        last_name="Doe",
        department="IT",
        base_salary=50000,
        educational_level=2,
        date_of_birth="11/09/1990",
        date_of_employment="11/09/2020",
        country="Denmark"
    )
    mock_response = 99999
    mocker.patch.object(emp, 'getSalary', return_value=mock_response)
    assert emp.getSalary() == mock_response

"""
Standalone test: Employee turns 18 tomorrow (should fail today, pass tomorrow)
This test will fail today because the person is 17, but will pass tomorrow when they turn 18.
"""
def test_employee_birthday_tomorrow_fails_today():
	emp = valid_employee()
	tomorrow = datetime.now() + timedelta(days=1)
	dob = tomorrow.replace(year=tomorrow.year - 18).strftime("%d/%m/%Y")
	with pytest.raises(ValueError):
		emp.set_date_of_birth(dob)

    