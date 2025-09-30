"""
Unit tests for Measure Converter Classes
Tests all conversion functionality for Length, Weight, Temperature, Currency, and Grade classes.
"""

import unittest
import os
import sqlite3
from unittest.mock import patch, MagicMock
import sys

# Add the app directory to the path to import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from Mesure_Converter import Length, Weight, Temperature, Currency, Grade


class TestLength(unittest.TestCase):
    """Test cases for Length converter."""
    
    def test_metric_to_imperial_conversion(self):
        """Test conversion from centimeters to inches."""
        length = Length(100, "Metric")
        result = length.convert()
        self.assertAlmostEqual(result, 39.37, places=2)
    
    def test_imperial_to_metric_conversion(self):
        """Test conversion from inches to centimeters."""
        length = Length(10, "Imperial")
        result = length.convert()
        self.assertAlmostEqual(result, 25.4, places=2)
    
    def test_invalid_system(self):
        """Test error handling for invalid system."""
        with self.assertRaises(ValueError):
            Length(100, "Invalid")
    
    def test_decimal_precision(self):
        """Test that results are rounded to 2 decimal places."""
        length = Length(1, "Metric")
        result = length.convert()
        self.assertEqual(len(str(result).split('.')[-1]), 2)


class TestWeight(unittest.TestCase):
    """Test cases for Weight converter."""
    
    def test_metric_to_imperial_conversion(self):
        """Test conversion from kilograms to pounds."""
        weight = Weight(70, "Metric")
        result = weight.convert()
        self.assertAlmostEqual(result, 154.32, places=2)
    
    def test_imperial_to_metric_conversion(self):
        """Test conversion from pounds to kilograms."""
        weight = Weight(154, "Imperial")
        result = weight.convert()
        self.assertAlmostEqual(result, 69.85, places=2)
    
    def test_invalid_system(self):
        """Test error handling for invalid system."""
        with self.assertRaises(ValueError):
            Weight(70, "Invalid")
    
    def test_decimal_precision(self):
        """Test that input is rounded to 2 decimal places."""
        weight = Weight(70.12345, "Metric")
        self.assertEqual(weight.measure, 70.12)


class TestTemperature(unittest.TestCase):
    """Test cases for Temperature converter."""
    
    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        temp = Temperature(25, "C")
        result = temp.convert("F")
        self.assertAlmostEqual(result, 77.0, places=2)
    
    def test_celsius_to_kelvin(self):
        """Test Celsius to Kelvin conversion."""
        temp = Temperature(25, "C")
        result = temp.convert("K")
        self.assertAlmostEqual(result, 298.15, places=2)
    
    def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion."""
        temp = Temperature(77, "F")
        result = temp.convert("C")
        self.assertAlmostEqual(result, 25.0, places=2)
    
    def test_fahrenheit_to_kelvin(self):
        """Test Fahrenheit to Kelvin conversion."""
        temp = Temperature(77, "F")
        result = temp.convert("K")
        self.assertAlmostEqual(result, 298.15, places=2)
    
    def test_kelvin_to_celsius(self):
        """Test Kelvin to Celsius conversion."""
        temp = Temperature(298.15, "K")
        result = temp.convert("C")
        self.assertAlmostEqual(result, 25.0, places=2)
    
    def test_kelvin_to_fahrenheit(self):
        """Test Kelvin to Fahrenheit conversion."""
        temp = Temperature(298.15, "K")
        result = temp.convert("F")
        self.assertAlmostEqual(result, 77.0, places=2)
    
    def test_same_scale_conversion(self):
        """Test conversion to same scale returns original value."""
        temp = Temperature(25, "C")
        result = temp.convert("C")
        self.assertEqual(result, 25.0)
    
    def test_invalid_scale(self):
        """Test error handling for invalid temperature scale."""
        with self.assertRaises(ValueError):
            Temperature(25, "X")
    
    def test_invalid_destination_scale(self):
        """Test error handling for invalid destination scale."""
        temp = Temperature(25, "C")
        with self.assertRaises(ValueError):
            temp.convert("X")
    
    def test_freezing_point_conversions(self):
        """Test conversions at water freezing point."""
        # 0°C = 32°F = 273.15K
        temp_c = Temperature(0, "C")
        self.assertAlmostEqual(temp_c.convert("F"), 32.0, places=2)
        self.assertAlmostEqual(temp_c.convert("K"), 273.15, places=2)
    
    def test_boiling_point_conversions(self):
        """Test conversions at water boiling point."""
        # 100°C = 212°F = 373.15K
        temp_c = Temperature(100, "C")
        self.assertAlmostEqual(temp_c.convert("F"), 212.0, places=2)
        self.assertAlmostEqual(temp_c.convert("K"), 373.15, places=2)


class TestCurrency(unittest.TestCase):
    """Test cases for Currency converter."""
    
    def test_currency_initialization(self):
        """Test currency initialization with valid code."""
        currency = Currency("USD")
        self.assertEqual(currency.base_currency, "USD")
    
    def test_invalid_currency_code_length(self):
        """Test error handling for invalid currency code length."""
        with self.assertRaises(ValueError):
            Currency("INVALID")
        
        with self.assertRaises(ValueError):
            Currency("US")
    
    def test_same_currency_conversion(self):
        """Test conversion to same currency returns original amount."""
        currency = Currency("USD")
        result = currency.convert(100, "USD")
        self.assertEqual(result, 100.0)
    
    @patch('requests.get')
    def test_successful_api_conversion(self, mock_get):
        """Test successful API currency conversion."""
        # Mock API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'data': {
                'EUR': 0.85,
                'GBP': 0.73
            }
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        currency = Currency("USD")
        result = currency.convert(100, "EUR")
        self.assertEqual(result, 85.0)
    
    @patch('requests.get')
    def test_api_request_error(self, mock_get):
        """Test handling of API request errors."""
        mock_get.side_effect = Exception("API Error")
        
        currency = Currency("USD")
        result = currency.convert(100, "EUR")
        self.assertIsNone(result)
    
    @patch('requests.get')
    def test_missing_currency_in_response(self, mock_get):
        """Test handling when requested currency is not in API response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': {'EUR': 0.85}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        currency = Currency("USD")
        result = currency.convert(100, "JPY")  # JPY not in mock response
        self.assertIsNone(result)


class TestGrade(unittest.TestCase):
    """Test cases for Grade converter."""
    
    def setUp(self):
        """Set up test database."""
        self.grade_converter = Grade()
        # Ensure database is created
        self.assertTrue(os.path.exists(self.grade_converter.db_path))
    
    def tearDown(self):
        """Clean up test database."""
        if os.path.exists(self.grade_converter.db_path):
            os.remove(self.grade_converter.db_path)
    
    def test_danish_to_american_conversion(self):
        """Test conversion from Danish to American grades."""
        result = self.grade_converter.convert(12, "Denmark")
        self.assertEqual(result, "A+")
        
        result = self.grade_converter.convert(10, "Denmark")
        self.assertEqual(result, "A")
        
        result = self.grade_converter.convert(7, "Denmark")
        self.assertEqual(result, "B")
    
    def test_american_to_danish_conversion(self):
        """Test conversion from American to Danish grades."""
        result = self.grade_converter.convert("A+", "America")
        self.assertEqual(result, "12")
        
        result = self.grade_converter.convert("A", "America")
        self.assertEqual(result, "10")
        
        result = self.grade_converter.convert("B", "America")
        self.assertEqual(result, "7")
    
    def test_invalid_country(self):
        """Test error handling for invalid country."""
        with self.assertRaises(ValueError):
            self.grade_converter.convert(12, "Invalid")
    
    def test_invalid_grade(self):
        """Test handling of invalid grades."""
        result = self.grade_converter.convert(99, "Denmark")  # Non-existent Danish grade
        self.assertIsNone(result)
        
        result = self.grade_converter.convert("Z", "America")  # Non-existent American grade
        self.assertIsNone(result)
    
    def test_database_creation(self):
        """Test that database is properly created and populated."""
        conn = sqlite3.connect(self.grade_converter.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM grade_conversions')
        count = cursor.fetchone()[0]
        self.assertGreater(count, 0)  # Should have grade mappings
        
        # Test specific mappings exist
        cursor.execute('SELECT american_grade FROM grade_conversions WHERE danish_grade = 12')
        result = cursor.fetchone()
        self.assertEqual(result[0], 'A+')
        
        conn.close()
    
    def test_case_insensitive_american_grades(self):
        """Test that American grade input is case insensitive."""
        result1 = self.grade_converter.convert("a", "America")
        result2 = self.grade_converter.convert("A", "America")
        self.assertEqual(result1, result2)


class TestIntegration(unittest.TestCase):
    """Integration tests for the measure converter system."""
    
    def test_multiple_conversions(self):
        """Test multiple conversions work correctly together."""
        # Length conversions
        length = Length(100, "Metric")
        inches = length.convert()
        
        # Weight conversions
        weight = Weight(70, "Metric")
        pounds = weight.convert()
        
        # Temperature conversions
        temp = Temperature(25, "C")
        fahrenheit = temp.convert("F")
        
        # Verify all conversions are reasonable
        self.assertGreater(inches, 0)
        self.assertGreater(pounds, 0)
        self.assertGreater(fahrenheit, 0)
    
    def test_round_trip_conversions(self):
        """Test that converting back and forth preserves original values."""
        # Length round trip
        original = 100
        length1 = Length(original, "Metric")
        converted = length1.convert()
        length2 = Length(converted, "Imperial")
        back_converted = length2.convert()
        self.assertAlmostEqual(original, back_converted, places=1)
        
        # Weight round trip
        original = 70
        weight1 = Weight(original, "Metric")
        converted = weight1.convert()
        weight2 = Weight(converted, "Imperial")
        back_converted = weight2.convert()
        self.assertAlmostEqual(original, back_converted, places=1)
    
    def test_extreme_values(self):
        """Test conversions with extreme values."""
        # Small values (use a value that won't round to 0)
        length = Length(1, "Metric")  # 1 cm should convert to ~0.39 inches
        result = length.convert()
        self.assertGreater(result, 0)
        
        # Very large values
        weight = Weight(10000, "Imperial")
        result = weight.convert()
        self.assertGreater(result, 0)
        
        # Absolute zero temperature (should be exactly 0K)
        temp = Temperature(-273.15, "C")
        kelvin = temp.convert("K")
        self.assertGreaterEqual(kelvin, 0)  # Should be 0 or very close to 0


if __name__ == '__main__':
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [TestLength, TestWeight, TestTemperature, TestCurrency, TestGrade, TestIntegration]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\nTest Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
