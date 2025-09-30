"""
Measure Converter Classes
Implements conversion between different measurement systems including:
- Length (Metric/Imperial)
- Weight (Metric/Imperial) 
- Temperature (Celsius/Fahrenheit/Kelvin)
- Currency (using API)
- Grades (Danish/American)
"""

import requests
import sqlite3
import os
from typing import Dict, Optional


class Length:
    """
    Conversion between Metric and Imperial length systems.
    Covers centimeters and inches.
    """
    
    def __init__(self, measure: float, system: str):
        """
        Constructor for Length converter.
        
        @param measure: The numeric measure to convert with up to two decimals
        @param system: The system of said measure (Metric or Imperial)
        """
        self.measure = round(float(measure), 2)
        self.system = system.lower()
        
        if self.system not in ['metric', 'imperial']:
            raise ValueError("System must be 'Metric' or 'Imperial'")
    
    def convert(self) -> float:
        """
        Convert between metric (cm) and imperial (inches).
        
        @return: The value of the conversion with up to two decimals
        """
        if self.system == 'metric':
            # Convert from centimeters to inches (1 inch = 2.54 cm)
            result = self.measure / 2.54
        else:
            # Convert from inches to centimeters
            result = self.measure * 2.54
        
        return round(result, 2)


class Weight:
    """
    Conversion between Metric and Imperial weight systems.
    Covers kilograms and pounds.
    """
    
    def __init__(self, measure: float, system: str):
        """
        Constructor for Weight converter.
        
        @param measure: The numeric measure to convert with up to two decimals
        @param system: The system of said measure (Metric or Imperial)
        """
        self.measure = round(float(measure), 2)
        self.system = system.lower()
        
        if self.system not in ['metric', 'imperial']:
            raise ValueError("System must be 'Metric' or 'Imperial'")
    
    def convert(self) -> float:
        """
        Convert between metric (kg) and imperial (pounds).
        
        @return: The value of the conversion with up to two decimals
        """
        if self.system == 'metric':
            # Convert from kilograms to pounds (1 kg = 2.20462 lbs)
            result = self.measure * 2.20462
        else:
            # Convert from pounds to kilograms
            result = self.measure / 2.20462
        
        return round(result, 2)


class Temperature:
    """
    Conversion between Celsius, Fahrenheit, and Kelvin temperature scales.
    """
    
    def __init__(self, measure: float, scale: str):
        """
        Constructor for Temperature converter.
        
        @param measure: The numeric measure to convert with up to two decimals
        @param scale: The temperature scale of said measure (C, F, or K)
        """
        self.measure = round(float(measure), 2)
        self.scale = scale.upper()
        
        if self.scale not in ['C', 'F', 'K']:
            raise ValueError("Scale must be 'C' (Celsius), 'F' (Fahrenheit), or 'K' (Kelvin)")
    
    def convert(self, destination_scale: str) -> float:
        """
        Convert temperature between scales using switch-like implementation.
        
        @param destination_scale: The destination temperature scale (C, F, or K)
        @return: The value of the conversion with up to two decimals
        """
        destination_scale = destination_scale.upper()
        
        if destination_scale not in ['C', 'F', 'K']:
            raise ValueError("Destination scale must be 'C', 'F', or 'K'")
        
        if self.scale == destination_scale:
            return self.measure
        
        # Switch implementation for 6 possible conversions
        conversion_key = f"{self.scale}_to_{destination_scale}"
        
        switch_conversions = {
            'C_to_F': self._celsius_to_fahrenheit,
            'C_to_K': self._celsius_to_kelvin,
            'F_to_C': self._fahrenheit_to_celsius,
            'F_to_K': self._fahrenheit_to_kelvin,
            'K_to_C': self._kelvin_to_celsius,
            'K_to_F': self._kelvin_to_fahrenheit
        }
        
        conversion_method = switch_conversions.get(conversion_key)
        if conversion_method:
            return round(conversion_method(), 2)
        else:
            raise ValueError(f"Conversion from {self.scale} to {destination_scale} not supported")
    
    def _celsius_to_fahrenheit(self) -> float:
        """Convert Celsius to Fahrenheit: F = (C × 9/5) + 32"""
        return (self.measure * 9/5) + 32
    
    def _celsius_to_kelvin(self) -> float:
        """Convert Celsius to Kelvin: K = C + 273.15"""
        return self.measure + 273.15
    
    def _fahrenheit_to_celsius(self) -> float:
        """Convert Fahrenheit to Celsius: C = (F - 32) × 5/9"""
        return (self.measure - 32) * 5/9
    
    def _fahrenheit_to_kelvin(self) -> float:
        """Convert Fahrenheit to Kelvin: K = (F - 32) × 5/9 + 273.15"""
        return (self.measure - 32) * 5/9 + 273.15
    
    def _kelvin_to_celsius(self) -> float:
        """Convert Kelvin to Celsius: C = K - 273.15"""
        return self.measure - 273.15
    
    def _kelvin_to_fahrenheit(self) -> float:
        """Convert Kelvin to Fahrenheit: F = (K - 273.15) × 9/5 + 32"""
        return (self.measure - 273.15) * 9/5 + 32


class Currency:
    """
    Conversion between world currencies using freecurrencyapi.net API.
    """
    
    def __init__(self, base_currency: str):
        """
        Constructor for Currency converter.
        
        @param base_currency: The base currency in 3-letter format (e.g., 'DKK')
        """
        self.base_currency = base_currency.upper()
        self.api_url = "https://api.freecurrencyapi.com/v1/latest"
        
        if len(self.base_currency) != 3:
            raise ValueError("Currency code must be 3 letters (e.g., 'USD', 'EUR', 'DKK')")
    
    def convert(self, amount: float, target_currency: str) -> Optional[float]:
        """
        Convert currency amount using freecurrencyapi.net API.
        
        @param amount: The numeric amount to convert with up to two decimals
        @param target_currency: The target currency code (3 letters)
        @return: The converted monetary amount with up to two decimals, or None if API fails
        """
        amount = round(float(amount), 2)
        target_currency = target_currency.upper()
        
        if len(target_currency) != 3:
            raise ValueError("Target currency code must be 3 letters")
        
        if self.base_currency == target_currency:
            return amount
        
        try:
            # Note: freecurrencyapi.net might require an API key for production use
            params = {
                'apikey': 'YOUR_API_KEY_HERE',  # Replace with actual API key
                'base_currency': self.base_currency
            }
            
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'data' in data and target_currency in data['data']:
                conversion_rate = data['data'][target_currency]
                converted_amount = amount * conversion_rate
                return round(converted_amount, 2)
            else:
                print(f"Currency {target_currency} not found in API response")
                return None
                
        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return None
        except Exception as e:
            print(f"Currency conversion error: {e}")
            return None


class Grade:
    """
    Conversion between Danish and American grading systems using local database.
    """
    
    def __init__(self):
        """Initialize Grade converter and create database if it doesn't exist."""
        self.db_path = os.path.join(os.path.dirname(__file__), 'grades.db')
        self._create_database()
    
    def _create_database(self):
        """Create and populate the grades database if it doesn't exist."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS grade_conversions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    danish_grade INTEGER,
                    american_grade TEXT,
                    description TEXT
                )
            ''')
            
            # Check if table is empty and populate it
            cursor.execute('SELECT COUNT(*) FROM grade_conversions')
            if cursor.fetchone()[0] == 0:
                # Danish 7-step scale to American letter grades
                grade_mappings = [
                    (12, 'A+', 'Excellent'),
                    (10, 'A', 'Very Good'),
                    (7, 'B', 'Good'),
                    (4, 'C', 'Fair'),
                    (2, 'D', 'Adequate'),
                    (0, 'F', 'Not Acceptable'),
                    (-3, 'F', 'Inadequate')
                ]
                
                cursor.executemany(
                    'INSERT INTO grade_conversions (danish_grade, american_grade, description) VALUES (?, ?, ?)',
                    grade_mappings
                )
                conn.commit()
            
            conn.close()
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def convert(self, grade, country: str) -> Optional[str]:
        """
        Convert grades between Danish and American systems.
        
        @param grade: The grade to convert
        @param country: The country whose grading system the grade corresponds to ('Denmark' or 'America')
        @return: The converted grade, or None if conversion fails
        """
        country = country.lower()
        
        if country not in ['denmark', 'america']:
            raise ValueError("Country must be 'Denmark' or 'America'")
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            if country == 'denmark':
                # Convert Danish grade to American
                grade = int(grade)
                cursor.execute(
                    'SELECT american_grade FROM grade_conversions WHERE danish_grade = ?',
                    (grade,)
                )
                result = cursor.fetchone()
                converted_grade = result[0] if result else None
                
            else:  # america
                # Convert American grade to Danish
                grade = str(grade).upper()
                cursor.execute(
                    'SELECT danish_grade FROM grade_conversions WHERE american_grade = ?',
                    (grade,)
                )
                result = cursor.fetchone()
                converted_grade = str(result[0]) if result else None
            
            conn.close()
            return converted_grade
            
        except (sqlite3.Error, ValueError) as e:
            print(f"Grade conversion error: {e}")
            return None


# Example usage and demonstration
if __name__ == "__main__":
    print("=== Measure Converter Demo ===\n")
    
    # Length conversion
    print("--- Length Conversion ---")
    length_metric = Length(100, "Metric")  # 100 cm
    print(f"100 cm = {length_metric.convert()} inches")
    
    length_imperial = Length(10, "Imperial")  # 10 inches
    print(f"10 inches = {length_imperial.convert()} cm\n")
    
    # Weight conversion
    print("--- Weight Conversion ---")
    weight_metric = Weight(70, "Metric")  # 70 kg
    print(f"70 kg = {weight_metric.convert()} lbs")
    
    weight_imperial = Weight(154, "Imperial")  # 154 lbs
    print(f"154 lbs = {weight_imperial.convert()} kg\n")
    
    # Temperature conversion
    print("--- Temperature Conversion ---")
    temp_celsius = Temperature(25, "C")
    print(f"25°C = {temp_celsius.convert('F')}°F")
    print(f"25°C = {temp_celsius.convert('K')}K")
    
    temp_fahrenheit = Temperature(77, "F")
    print(f"77°F = {temp_fahrenheit.convert('C')}°C")
    print(f"77°F = {temp_fahrenheit.convert('K')}K\n")
    
    # Grade conversion
    print("--- Grade Conversion ---")
    grade_converter = Grade()
    print(f"Danish grade 12 = American grade {grade_converter.convert(12, 'Denmark')}")
    print(f"American grade A = Danish grade {grade_converter.convert('A', 'America')}")
    
    print("\n=== Demo Complete ===")
