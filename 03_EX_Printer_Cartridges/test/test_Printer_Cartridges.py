import pytest
from app.Printer_Cartridges import cartridges

class TestCartridges:


    @pytest.mark.parametrize('cartridges, discount', [
        (5, "no discound"),       # Partition 5-99: lower valid boundary
    ])
    def test_cartridges_passes(self, cartridges, discount):
        assert cartridges(cartridges) == discount
        
    #
    # Positive testing
    #

    # Valid equivalence partition: 5-99 (no discount)
    @pytest.mark.parametrize('amount', [5, 6, 52, 98, 99])
    def test_no_discount(self, amount):
        assert cartridges(amount) == "no discound"

    # Valid equivalence partition: 100 and above (20% discount)
    @pytest.mark.parametrize('amount', [100, 101, 150])
    def test_20_percent_discount(self, amount):
        assert cartridges(amount) == "you get 20% discound"

    #
    # Negative testing
    #

    # Invalid: zero or negative (ValueError: "Amount cannot be zero or negative")
    @pytest.mark.parametrize('amount', [0, -1, -10])
    def test_zero_or_negative_raises_specific_valueerror(self, amount):
        with pytest.raises(ValueError) as excinfo:
            cartridges(amount)
        assert str(excinfo.value) == "Amount cannot be zero or negative"

    # Invalid: less than 5 but positive (ValueError: "Amount must be at least 5")
    @pytest.mark.parametrize('amount', [1, 3, 4])
    def test_less_than_five_raises_specific_valueerror(self, amount):
        with pytest.raises(ValueError) as excinfo:
            cartridges(amount)
        assert str(excinfo.value) == "Amount must be at least 5"