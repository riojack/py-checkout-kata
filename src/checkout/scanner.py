from functools import reduce


class Scanner:
    def __init__(self, price_model):
        self.items = []
        self.price_model = price_model

    def scan(self, item):
        self.items.append(item)
        return self

    def total(self):
        return reduce(self.__total_calculation_reducer, self.items, 0)

    def items_scanned(self):
        return [x for x in self.items]

    def __total_calculation_reducer(self, accumulator, current_item):
        price, _ = self.price_model.look_up_product(current_item)
        return accumulator + price
