from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# myMenuItem = MenuItem()
my_menu = Menu()
item = "0"


def run_program():
    response = input(f"What would you like? :{my_menu.get_items()}? ")
    if response == "report":
        print(f"{coffee_maker.report()}")
        print(f"{money_machine.report()}")
        run_program()
    # elif coffee_maker.is_resource_sufficient(response):
    elif response == 'off':
        return
    else:
        item = my_menu.find_drink(response)
        if coffee_maker.is_resource_sufficient(item) and (money_machine.make_payment(item.cost)):
            coffee_maker.make_coffee(item)
            run_program()
        else:
            print("I'm sorry, but your item is unavailable. Try again.")
            run_program()


# def pay(item):


run_program()
