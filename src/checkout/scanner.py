class Scanner:
    def __init__(self, price_model):
        self.price_model = price_model

    def scan(self, item):
        pass

    def total(self):
        return self.price_model.look_up_price('orange')
