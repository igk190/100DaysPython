from platform import machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
latte = MenuItem("latte", 200,150,24,2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino",250,50,24,3)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso €1.5/latte €2.5/cappuccino €3):").lower()
    options = ["off", "report", "latte", "espresso", "cappuccino"]
    while choice not in options:
        choice = input("Please try again. What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        resources_available = coffee_maker.is_resource_sufficient(menu.find_drink((choice)))
        if resources_available:
            # total_inserted = money_machine.process_coins()
            # print(f"You've inserted: ${total_inserted}")
            drink = menu.find_drink(choice)
            received_enough_money = money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)






