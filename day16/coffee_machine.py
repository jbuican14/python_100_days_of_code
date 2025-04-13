# See PyCharm help at https://www.jetbrains.com/help/pycharm/
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
    "coffee": 100
}

profit = 0

# "What would you like? (espresso/latte/cappuccino): after the answer"
def ask_for_money():
    """ Returns the total calculated from coins inserted """
    quarters = int(input("how many quarters?:") or 0) * 25
    dimes = int(input("how many dimes?:") or 0) * 10
    nickles = int(input("how many nickles?:") or 0) * 5
    pennies = int(input("how many pennies?:") or 0)
    return quarters + dimes + nickles + pennies


def update_resources(ingredients):
    # print(ingredients)
    for x in ingredients:
        resources[x] = resources[x]-ingredients[x]
    # print('resources new .>>>', resources)
def order_coffee():
    answer = input("What would you like? (espresso/latte/cappuccino):").lower() or 'off'
    # print("answer: ", answer)
    if answer == "off":
        exit()
    elif answer == "report":
        global profit
        print(f"Report is here:{resources} ${profit}")
        order_coffee()
    else:
        resource_coffee = MENU.get(answer) or "off"
        if resource_coffee == "off":
            exit()
        resource_coffee.get("ingredients")
        for x in resource_coffee["ingredients"]:
            if resources[x] < resource_coffee["ingredients"][x]:
                print(f"Sorry there is not enough {x}")
                order_coffee()
                return
        received_money = ask_for_money()
        is_enough_money = int(received_money) >= resource_coffee.get("cost")*100
        if not is_enough_money:
            print("Sorry that's not enough money. Money refunded.")
            order_coffee()
        else:
            changes = resource_coffee.get("cost")*100 - received_money
            update_resources(resource_coffee["ingredients"])
            profit += resource_coffee.get("cost")
            print(f"Here is ${changes/100} in change.")
            print(f"Here is your {answer} ☕️. Enjoy!")

        order_coffee()

order_coffee()

