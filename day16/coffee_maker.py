# https://pypi.org/project/colorama/
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        # table = PrettyTable()
        table = ColorTable(theme=Themes.OCEAN)
        table.add_column("Coffee resources", ["water", "milk", "coffee"])
        table.add_column("Qty", [str(self.resources['water']) +"ml", str(self.resources['milk']) +"ml", str(self.resources['coffee']) +"g"])
        table.align = 'l'
        print(table)

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refilled_coffee(self):
        """Fill the ingredients to the resources."""
        for item in self.resources:
            self.resources['water'] += 300
            self.resources['milk'] += 300
            self.resources['coffee'] += 30
        print(f"Refilled resources finished! and here is your report")
        self.report()
