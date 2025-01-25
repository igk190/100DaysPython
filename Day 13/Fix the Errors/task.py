try:
    age = int(input("How old are you?"))
except ValueError:
    print("You've typed an invalid number. Please try again.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print("Sorry you are too young.")