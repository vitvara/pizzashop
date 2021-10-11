from enum import Enum
from typing import Type

class PizzaSize(Enum):
    small = 120
    medium = 200
    large = 280


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size , PizzaSize):
            raise TypeError("size must be a PizzaSize")
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        price = self.size.value + 20*len(self.toppings)
        return price
    
    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        description = "A " + self.size.name
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain cheeze pizza"
        return description