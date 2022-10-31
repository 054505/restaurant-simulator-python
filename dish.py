class Dish:
    def __init__(self):
        self.name = ""
        self.price = 0

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            raise Exception("Price cannot be less than zero.")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name