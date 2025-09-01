# Roman numeral to decimal conversion

def roman_to_decimal(roman: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Rules for valid subtractive combinations
    subtractives = {
        'I': ['V', 'X'],
        'X': ['L', 'C'],
        'C': ['D', 'M']
    }
    total = 0
    prev_value = 0
    repeat_count = 1
    last_char = ''
    for i, char in enumerate(roman):
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        value = roman_values[char]
        # Check for repeats
        if char == last_char:
            repeat_count += 1
            if char in ['V', 'L', 'D']:
                raise ValueError(f"{char} cannot be repeated.")
            if repeat_count > 3:
                raise ValueError(f"{char} cannot be repeated more than 3 times.")
        else:
            repeat_count = 1
        # Subtractive notation
        if prev_value and value > prev_value:
            if last_char not in subtractives or char not in subtractives[last_char]:
                raise ValueError(f"Invalid subtractive combination: {last_char}{char}")
            total += value - 2 * prev_value  # Remove prev_value added last time, then subtract
        else:
            total += value
        prev_value = value
        last_char = char
    if total > 3999:
        raise ValueError("Value exceeds maximum representable Roman numeral (3999).")
    return total
