class InvalidProductPriceError(Exception):
    """Raised when a price has invalid value"""

    def __init__(self, price_limit):
        self.price_limit = price_limit

    def __str__(self):
        return f'{self.price_limit} can"t be <= 0.'
