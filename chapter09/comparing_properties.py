# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, another: "RealProperty"):
        return self.square_metres > another.square_metres

    def price_difference(self, another: "RealProperty"):
        self_price = self.square_metres * self.price_per_sqm
        another_price = another.square_metres * another.price_per_sqm
        if self_price > another_price:
            return self_price - another_price
        else:
            return another_price - self_price

    def more_expensive(self, another: "RealProperty"):
        self_total_price = self.square_metres * self.price_per_sqm
        another_total_price = another.square_metres * another.price_per_sqm

        return self_total_price > another_total_price
