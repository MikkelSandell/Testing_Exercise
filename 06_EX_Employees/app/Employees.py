from datetime import datetime

class Employee:
    def __init__(self, cpr, first_name, last_name, department, base_salary, educational_level, date_of_birth, date_of_employment, country):
        self.set_cpr(cpr)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_department(department)
        self.set_base_salary(base_salary)
        self.set_educational_level(educational_level)
        self.set_date_of_birth(date_of_birth)
        self.set_date_of_employment(date_of_employment)
        self.set_country(country)

    # CPR
    def get_cpr(self):
        return self.__cpr
    def set_cpr(self, value):
        if isinstance(value, str) and value.isdigit() and len(value) == 10:
            self.__cpr = value
        else:
            raise ValueError("CPR must be a string of 10 digits.")

    # First name
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 30 and all(c.isalpha() or c in [' ', '-'] for c in value):
            self.__first_name = value
        else:
            raise ValueError("First name must be 1-30 alphabetic characters, spaces or dashes.")

    # Last name
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 30 and all(c.isalpha() or c in [' ', '-'] for c in value):
            self.__last_name = value
        else:
            raise ValueError("Last name must be 1-30 alphabetic characters, spaces or dashes.")

    # Department
    def get_department(self):
        return self.__department
    def set_department(self, value):
        allowed = ['HR', 'Finance', 'IT', 'Sales', 'General Services']
        if value in allowed:
            self.__department = value
        else:
            raise ValueError(f"Department must be one of {allowed}.")

    # Base salary
    def get_base_salary(self):
        return self.__base_salary
    def set_base_salary(self, value):
        if isinstance(value, (int, float)) and 20000 <= value <= 100000:
            self.__base_salary = value
        else:
            raise ValueError("Base salary must be between 20000 and 100000.")

    # Educational level
    def get_educational_level(self):
        levels = {0: "none", 1: "primary", 2: "secondary", 3: "tertiary"}
        return levels.get(self.__educational_level, "unknown")
    def set_educational_level(self, value):
        if value in [0, 1, 2, 3]:
            self.__educational_level = value
        else:
            raise ValueError("Educational level must be 0, 1, 2, or 3.")

    # Date of birth
    def get_date_of_birth(self):
        return self.__date_of_birth
    def set_date_of_birth(self, value):
        try:
            dob = datetime.strptime(value, "%d/%m/%Y")
        except Exception:
            raise ValueError("Date of birth must be in dd/MM/yyyy format.")
        today = datetime.now()
        if (today - dob).days >= 18 * 365:
            self.__date_of_birth = value
        else:
            raise ValueError("Employee must be at least 18 years old.")

    # Date of employment
    def get_date_of_employment(self):
        return self.__date_of_employment
    def set_date_of_employment(self, value):
        try:
            doe = datetime.strptime(value, "%d/%m/%Y")
        except Exception:
            raise ValueError("Date of employment must be in dd/MM/yyyy format.")
        today = datetime.now()
        if doe <= today:
            self.__date_of_employment = value
        else:
            raise ValueError("Date of employment cannot be in the future.")

    # Country
    def get_country(self):
        return self.__country
    def set_country(self, value):
        if isinstance(value, str) and value:
            self.__country = value
        else:
            raise ValueError("Country must be a non-empty string.")

    # Actual salary
    def getSalary(self):
        return self.__base_salary + (self.__educational_level * 1220)

    # Discount
    def getDiscount(self):
        doe = datetime.strptime(self.__date_of_employment, "%d/%m/%Y")
        today = datetime.now()
        years = (today - doe).days // 365
        return years * 0.5

    # Shipping costs
    def getShippingCosts(self):
        nordic_free = ["Denmark", "Norway", "Sweden"]
        nordic_half = ["Iceland", "Finland"]
        if self.__country in nordic_free:
            return 0
        elif self.__country in nordic_half:
            return 50
        else:
            return 100
