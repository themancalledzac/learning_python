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


def run_program():
    response = input("What would you like? (espresso/latte/cappuccino): ")
    # print(response)
    if response == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
        run_program()
    elif response not in ["espresso", "latte", "cappuccino"]:
        print("Please select a valid response. ")
        run_program()
    else:
        pay(response)


def pay(response):
    total = MENU[response]["cost"]
    print(f"Cost is ${total}")
    ingredients = MENU[response]["ingredients"]
    # print(order)
    print("Please insert coins.")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")
    payment = calculate(int(quarters), int(dimes), int(nickles), int(pennies))
    change = payment - total
    enough = check_resources(ingredients, resources)
    if change >= 0:
        if enough == True:
            change_resources(ingredients)
            print(f"Here is ${change}.")
            print(f"Here is your {response}. Enjoy!")
            run_program()
        else:
            print("Sorry, not enough ingredients. ")
            run_program()
    else:
        print("Sorry, that is not enough money. Money refunded.")
        run_program()


def calculate(q, d, n, p):
    total = ((q * 25) + (d * 10) + (n * 5) + (p)) / 100
    return total


def check_resources(order, stock):
    while (stock["water"] > order["water"]) and (stock["milk"] > order["milk"]) and (stock["coffee"] > order["coffee"]):
        return True
    return False


def change_resources(order):
    global resources
    resources["water"] -= order["water"]
    resources["milk"] -= order["milk"]
    resources["coffee"] -= order["coffee"]


run_program()
