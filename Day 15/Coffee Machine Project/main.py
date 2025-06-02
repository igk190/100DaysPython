menu = {
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
    "water": 300, # resources["water"] -= 200
    "milk": 200,
    "coffee": 100, # g
    "money": 0
}
def is_resources_sufficient(order_ingredients):
    """ Checks if resources are sufficient to make a drink."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
        else:
            return True

def calculate_value(quarters, dimes, nickles, pennies):
    """ Calculates total value of inserted coins. """
    total_value = 0
    total_value += (quarters * 0.25)
    total_value += (dimes * 0.10)
    total_value += (nickles * 0.05)
    total_value += (pennies * 0.01)
    print(f"Total value cash: {total_value}")
    return total_value

def has_enough_money(drink, cash):
    """Checks if user inserted enough cash to afford the drink. """
    if cash >= drink:
        return True
    else:
        return False

def update_resources(drink):
    resources["water"] -= drink["water"]
    if "milk" in drink.keys():
        resources["milk"] -= drink["milk"]
    resources["coffee"] -= drink["coffee"]

machine_off = False
while not machine_off:
    user_choice = input("What would you like? (espresso €1.5/latte €2.5/cappuccino €3):").lower()

    options = ["off", "report", "espresso","latte","cappuccino"]
    while user_choice not in options: # make sure user inputs valid command from available options
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # Check machine
    if user_choice == "off":
        print("Scheduling for maintenance.")
        machine_off = True
    elif user_choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${resources['money']}")
    else: # assume user wants to order a drink
        drink = menu[user_choice]
        is_resources_sufficient(drink["ingredients"])

        print("Please insert coins.")
        quarters = int(input("How many quarters? $0.25"))
        dimes = int(input("How many dimes? $0.10"))
        nickles = int(input("How many quarters? $0.05"))
        pennies = int(input("How many quarters? $0.01"))
        cash = calculate_value(quarters, dimes, nickles, pennies)

        if has_enough_money(drink["cost"], cash):
            print("Just a moment, we're brewing your coffee...")

            resources["money"] = cash
            change = round(cash - drink["cost"],2)
            resources["money"] -= change
            # print(f"Resources after giving change {resources['money']}")

            if change > 0:
                print(f"Here's ${change} in change.")

            update_resources(drink["ingredients"])
            print(f"Here is your {user_choice}. Enjoy! ☕️😊")
        else:
            print("Sorry that's not enough money. Money refunded.")


""" What I've learned on Day 15:

1.  At first try, I tried something like:

    for items in resources.items():
            print(items["water"])
            
    Which looks like:
    ('water', 300)
    ('milk', 200)
    ('coffee', 100)
    ('money', 0) but this doesn't show the measurement unit.
    Looking at the solution video taught me this is better: 
        print(f"Money: ${resources['money']}")
        
2. I was 'stuck' figuring out how to access and compare (!) key-value pairs from 2 dicts.
I didn't consider searching the dict VIA the user's drink. drink = menu[user_choice]. This prints latte entry.
Now we can check it's ingredients and loop through them, comparing them against resources.

Need more practice with this.

3. Once you start writing bigger chunks of code, put into separate functions! Much easier to read.

4. from solution: def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]. Because items are the same!

"""