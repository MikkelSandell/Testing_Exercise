def cartridges(amount: int) -> str:
    if amount <= 0:
        raise ValueError("Amount cannot be zero or negative")
    if amount < 5:
        raise ValueError("Amount must be at least 5")
    if amount >= 100:
        return "you get 20% discound"
    return "no discound"