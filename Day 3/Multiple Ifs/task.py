print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Yay! You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill +- 5
        print("The ticket price is $5.")
    elif age <= 18:
        bill += 7
        print("The ticket price is $7.")
    else:
        bill += 12
        print("The ticket price is $12.")

    wants_photo = input('Do you want a photo? A photo costs $2 extra. Type Y or N')
    if wants_photo == "Y":
        bill += 2
        print(f"Please pay ${bill}")
    else:
        print(f"Please pay ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
