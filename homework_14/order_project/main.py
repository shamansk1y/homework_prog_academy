import module_product_order
import module_buyer_order
import module_order_order

if __name__ == '__main__':
    product_1 = module_product_order.Product('Top Flex', 1550, "Futsal shoes", "TOPS2022IN", "43", "Joma", "Spain")
    product_2 = module_product_order.Product('Tornado', 1450, "Official match ball", "2214008", "4", "Select", "Denmark")
    product_3 = module_product_order.Product('T-shirt Ucrania UAF', 1350, "Official match t-shirt", "AT102404A709", "Medium", "Joma", "Spain")
    product_4 = module_product_order.Product('Estadio III', 650, "Training bag", "400234.100", "ONESIZE", "Joma", "Spain")

    buyer_1 = module_buyer_order.Buyer("John", "Doe", "+38-096-111-11-11", "john_doe@gmail.com")
    buyer_2 = module_buyer_order.Buyer("Jane", "Doe", "+38-096-222-22-22", "jane_doe@gmail.com")

    order_0001 = module_order_order.Order("Order №0001", buyer_1)
    order_0001.add_product(product_1)
    order_0001.add_product(product_2)
    order_0001.add_product(product_3)
    print(order_0001)

    order_0002 = module_order_order.Order("Order №0002", buyer_2)
    order_0002.add_product(product_4)
    order_0002.add_product(product_2)
    order_0002.add_product(product_1)
    print(order_0002)
