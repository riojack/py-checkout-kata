class PriceModel:
    def __init__(self):
        self.__product_price_dict = {}

    def add(self, product_name, product_price):
        self.__product_price_dict[product_name] = product_price
        return self

    def look_up_price(self, product_name):
        return self.__product_price_dict[product_name]
