from turtledemo.penrose import start
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
math_dict["*"](4, 8)

print(art.logo)
should_continue = True
user_number_1 = int(input("Type the first number: "))
# calc_result = 0
while should_continue:
    user_operator = input("Type a mathematical operator:\n +\n -\n *\n /\n")
    user_number_2 = int(input("Type the second number: "))
    result = math_dict[user_operator](user_number_1,user_number_2)
    print(f"The result of {user_number_1} {user_operator} {user_number_2} = {result}")
    wants_more_math = input(f"Type 'y' to continue calculating with {result}. Type 'n' to start from scratch.")
    if wants_more_math == 'y':
        user_number_1 = result
    else:
        user_number_1 = int(input("Type the first number: "))