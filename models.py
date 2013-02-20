from django.db import models
from money import Currency, CURRENCY
from decimal import Decimal


class ExchangeRate:
    primary = Currency()
    secondary = Currency()
    value = Decimal("0.0")

    def __init__(self, primary, secondary, value):
        self.primary = primary
        self.secondary = secondary
        self.value = value
