from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal


def valid_curr_code(code):
    """Checks if given code is included as valid currency code in forex

        >>> valid_curr_code('USD')
        True
        >>> valid_curr_code('DOG')
        False
    """
    if code == "":
        return False

    c = CurrencyRates()
    try:
        c.get_rates(code)
    except:
        return False
    else:
        return True


def valid_amount(amount):
    """Takes an amount as string, Returns True if value larger than 0

        >>> valid_amount("5")
        True
        >>> valid_amount(10.10)
        True
        >>> valid_amount("")
        False
        >>> valid_amount("-50")
        False
        >>> valid_amount("dog")
        False
    """
    try:
        dec_amount = Decimal(amount)
    except:
        return False

    if dec_amount < 0:
        return False
    else:
        return True


def get_target_currency_symbol(conv_to):
    """Return currency symbol based on given currency code in forex

        >>> get_target_currency_symbol('GBP')
        '\xa3'
        >>> get_target_currency_symbol('DOG')
        ''
    """
    codes = CurrencyCodes()

    symbol = codes.get_symbol(conv_to)
    if symbol == None:
        return ''
    else:
        return f"{symbol}"


def convert_currency(start_curr, end_curr, amount):
    """Covert start currency to end currency using current conversion rate
        in forex. Return converted amount rounded to 2 places

        >>> convert_currency('USD', 'USD', 1)
        Decimal('1.00')
        >>> convert_currency('EUR', 'EUR', 2.45)
        Decimal('2.45')
        >>> convert_currency('GBP', 'GBP', '2000')
        Decimal('2000.00')
    """

    rates = CurrencyRates(force_decimal=True)

    return round(rates.convert(start_curr, end_curr, Decimal(amount)), 2)
