print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 "))

#tip_converted = round((100 + tip) // 100, 2)
tip += 100
tip /= 100
print(tip)

bill_incl_tip = round(bill * tip)
print(f"The total price including tips is: {bill_incl_tip}")

people = int(input("How many people to split the bill? "))

price_per_person = round(bill_incl_tip / people,2)
#print(price_per_person)

print(f"Each person has to pay {price_per_person}, tips included.")


