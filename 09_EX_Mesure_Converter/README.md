# Measure Converter

A comprehensive Python library for converting between different measurement systems including Length, Weight, Temperature, Currency, and Grade conversions.

## Features

### 🔧 Length Converter
- **Systems**: Metric (centimeters) ↔ Imperial (inches)
- **Usage**: `Length(measure, system).convert()`
- **Example**: Convert 100 cm to inches

### ⚖️ Weight Converter  
- **Systems**: Metric (kilograms) ↔ Imperial (pounds)
- **Usage**: `Weight(measure, system).convert()`
- **Example**: Convert 70 kg to pounds

### 🌡️ Temperature Converter
- **Scales**: Celsius ↔ Fahrenheit ↔ Kelvin
- **Usage**: `Temperature(measure, scale).convert(destination_scale)`
- **Example**: Convert 25°C to Fahrenheit or Kelvin

### 💱 Currency Converter
- **Source**: freecurrencyapi.net API
- **Usage**: `Currency(base_currency).convert(amount, target_currency)`
- **Note**: Requires API key for production use

### 🎓 Grade Converter
- **Systems**: Danish (7-step scale) ↔ American (letter grades)
- **Usage**: `Grade().convert(grade, country)`
- **Database**: Local SQLite database with grade mappings

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd 09_EX_Mesure_Converter

# Install dependencies using Poetry
poetry install

# Or using pip
pip install requests
```

## Quick Start

```python
from app.Mesure_Converter import Length, Weight, Temperature, Grade

# Length conversion
length = Length(100, "Metric")  # 100 cm
inches = length.convert()  # Returns 39.37 inches

# Weight conversion  
weight = Weight(70, "Metric")  # 70 kg
pounds = weight.convert()  # Returns 154.32 lbs

# Temperature conversion
temp = Temperature(25, "C")  # 25°C
fahrenheit = temp.convert("F")  # Returns 77.0°F
kelvin = temp.convert("K")     # Returns 298.15K

# Grade conversion
grade_converter = Grade()
american_grade = grade_converter.convert(12, "Denmark")  # Returns "A+"
danish_grade = grade_converter.convert("A", "America")   # Returns "10"
```

## API Reference

### Length Class
```python
Length(measure: float, system: str)
```
- `measure`: Numeric value to convert (up to 2 decimals)
- `system`: "Metric" (cm) or "Imperial" (inches)
- `convert()`: Returns converted value

### Weight Class  
```python
Weight(measure: float, system: str)
```
- `measure`: Numeric value to convert (up to 2 decimals)
- `system`: "Metric" (kg) or "Imperial" (lbs)
- `convert()`: Returns converted value

### Temperature Class
```python
Temperature(measure: float, scale: str)
```
- `measure`: Numeric value to convert (up to 2 decimals)
- `scale`: "C" (Celsius), "F" (Fahrenheit), or "K" (Kelvin)
- `convert(destination_scale: str)`: Returns converted value

### Currency Class
```python
Currency(base_currency: str)
```
- `base_currency`: 3-letter currency code (e.g., "USD", "EUR", "DKK")
- `convert(amount: float, target_currency: str)`: Returns converted amount or None if API fails

### Grade Class
```python
Grade()
```
- `convert(grade, country: str)`: Convert between Danish and American grades
- `country`: "Denmark" or "America"

## Grade Conversion Table

| Danish Grade | American Grade | Description |
|--------------|----------------|-------------|
| 12 | A+ | Excellent |
| 10 | A | Very Good |
| 7 | B | Good |
| 4 | C | Fair |
| 2 | D | Adequate |
| 0 | F | Not Acceptable |
| -3 | F | Inadequate |

## Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=app

# Run specific test file
python test/test_Mesure_Converter.py
```

## Currency API Setup

To use the Currency converter in production:

1. Sign up at [freecurrencyapi.net](https://freecurrencyapi.net/)
2. Get your API key
3. Replace `'YOUR_API_KEY_HERE'` in the Currency class with your actual API key

## Error Handling

All converters include comprehensive error handling:
- **Invalid input validation**
- **API failure handling** (Currency)
- **Database error handling** (Grade)
- **Precision control** (2 decimal places)

## Examples

### Complete Conversion Workflow
```python
# Import all converters
from app.Mesure_Converter import Length, Weight, Temperature, Currency, Grade

# Convert a recipe from metric to imperial
flour_metric = Weight(500, "Metric")  # 500g flour
flour_imperial = flour_metric.convert()  # 1.10 lbs

oven_celsius = Temperature(180, "C")  # 180°C oven
oven_fahrenheit = oven_celsius.convert("F")  # 356°F

print(f"Recipe: {flour_imperial} lbs flour, bake at {oven_fahrenheit}°F")
```

### Educational Grade Comparison
```python
grade_converter = Grade()

danish_grades = [12, 10, 7, 4, 2, 0, -3]
print("Danish → American Grade Conversion:")
for danish_grade in danish_grades:
    american = grade_converter.convert(danish_grade, "Denmark")
    print(f"{danish_grade} → {american}")
```

## Project Structure

```
09_EX_Mesure_Converter/
├── app/
│   ├── __init__.py
│   └── Mesure_Converter.py     # Main converter classes
├── test/
│   ├── __init__.py
│   └── test_Mesure_Converter.py # Comprehensive test suite
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is open source and available under the MIT License.