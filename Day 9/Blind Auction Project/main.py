from art import logo

def find_highest_bidder(dict):
    highest_bid = 0
    for value in dict.values():
        if value > highest_bid:
            highest_bid = value
    for name, bid in dict.items():
        if bid == highest_bid:
            print(f"The highest bidder is {name} with a bid of {bid}")

print(logo)
print("Welcome to the secret auction program.")

bids = {}

add_people = True
while add_people:
    name = input("What is your name?")
    bid = int(input("What's your bid?"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
    print("\n" * 30)
    if should_continue == "no":
        add_people = False

winning_bid = find_highest_bidder(bids)


