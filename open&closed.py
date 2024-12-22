from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class NoDiscount(Discount):
    def apply_discount(self, amount):
        return amount


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)



discount = PercentageDiscount(20)
print(discount.apply_discount(100))  
