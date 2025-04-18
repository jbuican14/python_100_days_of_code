# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_continue = True

while is_continue:
    choice = input(f"What would you like? {menu.get_items()}").lower().strip() or 'no idea'
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_continue = False
    elif choice == 'refill':
        coffee_maker.refilled_coffee()
    elif choice != (menu.find_drink(choice) == 'None'):
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
