from prettytable.colortable import ColorTable, Theme
#print beautiful table

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        # table = ColorTable(theme=Theme.format_code("\x1b90,\x1b90,\x1b90,\x1b90"))
        table = ColorTable(theme=Theme(vertical_char="|", default_color="35",vertical_color="34",horizontal_color="34",
        junction_color="16",))
        table.field_names =["Sales", "Total"]
        table.add_row(["Money " , str(self.CURRENCY )+ str(self.profit)])
        table.align = 'l'
        print(table)
        # print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ") or 0) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
