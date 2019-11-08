class PriceModel:
    def __init__(self):
        self.__product_price_dict = {}

    def add_product(self, product_name, product_price):
        self.__product_price_dict[product_name] = (product_price, sold_by_unit())
        return self

    def look_up_product(self, product_name):
        return self.__product_price_dict.get(product_name, (0.0, sold_by_unit()))


def sold_by_unit():
    return 'sold by unit'


def sold_by_weight():
    return 'sold by weight'
