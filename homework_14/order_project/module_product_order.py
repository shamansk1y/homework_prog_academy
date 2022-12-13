import module_ex_price_order
class Product():
    def __init__(self, product_name: str, price: int, description: str, vendor_code: str, size: str, brand: str, producing_country: str):
        """
        Function for typical created new product
        :param product_name: product name
        :param price: product price
        :param description: description of product
        :param vendor_code: vendor code of product
        :param size: product size
        :param brand: brand name
        :param producing_country: producing country of product
        """
        self.price = price
        if price <= 0:
            raise module_ex_price_order.InvalidProductPriceError(self.price)
        self.product_name = product_name
        self.description = description
        self.vendor_code = vendor_code
        self.size = size
        self.brand = brand
        self.producing_country = producing_country

    def __str__(self):
        return f'{self.brand} {self.product_name} - {self.vendor_code} === {self.price}.00 UAH'