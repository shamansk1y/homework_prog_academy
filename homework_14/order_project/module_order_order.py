import module_product_order
import module_buyer_order
import module_order_iter
import module_user_seq

class Order():
    def __init__(self, order_numder: str, buyer: module_buyer_order.Buyer):
        """
        Function for created new order
        :param order_numder: order number must be unique
        :param buyer: contact buyer info, used from class Buyer
        """
        self.order_numder = order_numder
        self.buyer = buyer
        self.total_order = []

    def add_product(self, product: module_product_order.Product):
        """
        Function that adds items to the cart
        :param product: product info, used from class Product
        :return:
        """
        self.total_order.append(product)

    def total(self):
        """
        Function for calculating the total amount of the order
        :return: total amount of the order
        """
        return sum(i.price for i in self.total_order)

    def __str__(self):
        return f"{self.order_numder}\nby {self.buyer}\n{'-' * 50}\n" + '\n'.join(map(str, self.total_order)) + '\n' + \
               'Total price: ' + f'{self.total()}.00' + " UAH" + '\n'

    def __iter__(self):
        return module_order_iter.OrderIter(self.total_order)

    def total_order(self):
        return module_user_seq.UserSequence(self.total_order)