from functools import reduce


class Scanner:
    def __init__(self, price_model):
        self.items = []
        self.price_model = price_model

    def scan(self, item):
        self.items.append(item)
        return self

    def total(self):
        return reduce(lambda accumulator, item: accumulator + self.price_model.look_up_product(item), self.items, 0)

    def items_scanned(self):
        return [x for x in self.items]
