# FUTURE IMPROVEMENT 
# add functionality to refill ingredient 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water, milk, coffee = resources["water"], resources["milk"], resources["coffee"]
cappuccino, latte, espresso = MENU["cappuccino"], MENU["latte"], MENU["espresso"]

profit = 0
quarters = 25
dimes = 10

nickles = 5
pennies = 1
is_continue  = True

# custom
def turn_off():
    exit()

# same
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

# 💪
"""Check if any item found insufficient, it will then return immediately"""
def check_resources(order_in):
    for item in order_in:
        if resources[item] < order_in[item]:
            print(f"Sorry there is not enough: {item}")
            return False
    return True


def process_coins(coins, cost):
    """ This will process coins and update the amount and add to profit. You can break it into different function """
    changes = 0
    if (coins*0.01) < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        changes = (coins*0.01) - cost
    if changes > 0:
        print(f"Here is ${changes} in change.")
    print(f"Here is {choice} ☕ ☕️ Enjoy!")


def adjust_resources():
    current_coffee = coffee_order["ingredients"]
    for resource in resources:
        if resources[resource] and current_coffee.get(resource, 0):
            resources[resource] = resources[resource] - current_coffee[resource]

while is_continue:
    choice = input("What would you like? (espresso/latte/cappuccino):").strip().lower()

    coffee_order = MENU.get(choice, "NOT FOUND")
    if coffee_order != "NOT FOUND":
        can_fulfill = check_resources(coffee_order["ingredients"])

        if can_fulfill:
            print("Please insert coins.")
            total = int(input("How many quarters?: ") or 0) * 25
            total += int(input("How many dimes?: ") or 0) * 10
            total += int(input("How many nickles?: ") or 0) * 5
            total += int(input("How many pennies?: ") or 0)
            process_coins(total, coffee_order["cost"])
            adjust_resources()
            profit += coffee_order["cost"]
    elif choice == 'report':
        print_report()
    elif choice == 'off':
        turn_off()

