from app.romen_numerals import roman_to_decimal
import pytest

#
# Positive testing
#
def test_roman_I_is_1():
    # Arrange
    roman = 'I'
    expected = 1
    # Act
    result = roman_to_decimal(roman)
    # Assert
    assert result == expected

def test_roman_V_is_5():
    assert roman_to_decimal('V') == 5

def test_roman_X_is_10():
    assert roman_to_decimal('X') == 10

def test_roman_L_is_50():
    assert roman_to_decimal('L') == 50

def test_roman_C_is_100():
    assert roman_to_decimal('C') == 100

def test_roman_D_is_500():
    assert roman_to_decimal('D') == 500

def test_roman_M_is_1000():
    assert roman_to_decimal('M') == 1000

def test_roman_III_is_3():
    assert roman_to_decimal('III') == 3

def test_roman_VIII_is_8():
    assert roman_to_decimal('VIII') == 8

def test_roman_XVII_is_17():
    assert roman_to_decimal('XVII') == 17

def test_roman_MDCCCLXVII_is_1867():
    assert roman_to_decimal('MDCCCLXVII') == 1867

def test_roman_IV_is_4():
    assert roman_to_decimal('IV') == 4

def test_roman_IX_is_9():
    assert roman_to_decimal('IX') == 9

def test_roman_XL_is_40():
    assert roman_to_decimal('XL') == 40

def test_roman_XC_is_90():
    assert roman_to_decimal('XC') == 90

def test_roman_CD_is_400():
    assert roman_to_decimal('CD') == 400

def test_roman_CM_is_900():
    assert roman_to_decimal('CM') == 900

def test_roman_XCIV_is_94():
    assert roman_to_decimal('XCIV') == 94

def test_roman_MMMCMXCIX_is_3999():
    assert roman_to_decimal('MMMCMXCIX') == 3999

#
# Negative testing
#
def test_invalid_repeat_I():
    with pytest.raises(ValueError):
        roman_to_decimal('IIII')

def test_invalid_repeat_V():
    with pytest.raises(ValueError):
        roman_to_decimal('VV')

def test_invalid_repeat_X():
    with pytest.raises(ValueError):
        roman_to_decimal('XXXX')

def test_invalid_repeat_L():
    with pytest.raises(ValueError):
        roman_to_decimal('LL')

def test_invalid_repeat_D():
    with pytest.raises(ValueError):
        roman_to_decimal('DD')

def test_invalid_subtractive_IL():
    with pytest.raises(ValueError):
        roman_to_decimal('IL')

def test_invalid_subtractive_IC():
    with pytest.raises(ValueError):
        roman_to_decimal('IC')

def test_invalid_subtractive_XM():
    with pytest.raises(ValueError):
        roman_to_decimal('XM')

def test_invalid_subtractive_VX():
    with pytest.raises(ValueError):
        roman_to_decimal('VX')

def test_invalid_subtractive_LC():
    with pytest.raises(ValueError):
        roman_to_decimal('LC')

def test_invalid_subtractive_DM():
    with pytest.raises(ValueError):
        roman_to_decimal('DM')

def test_exceeds_maximum():
    with pytest.raises(ValueError):
        roman_to_decimal('MMMM')

#
# Data type testing
#
def test_roman_to_decimal_returns_int():
    assert isinstance(roman_to_decimal('X'), int)
