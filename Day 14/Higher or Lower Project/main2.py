from art import logo, vs
from game_data import data # 50 items
import random

score = 0
game_over = False

print(logo)
list_length = len(data)

item_b = random.choice(data)

def is_correct(choice, a, b):
    """Check if user guessed correctly and give feedback"""
    if item_a["follower_count"] > item_b["follower_count"]:
        return user_choice == "A"
    else: # choice = "B"
        return user_choice == "B"

while not game_over:
    item_a = item_b
    item_b = random.choice(data)
    # check if duplicate
    if item_a == item_b:
        item_b = random.choice(data)

    print(f"Compare A: {item_a['name']}, a {item_a['description']} from {item_a['country']}")
    print(vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']} from {item_b['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B'").upper()

    options = ["A", "B"]
    while not user_choice in options:
        user_choice = input("Who has more followers? Type 'A' or 'B'").upper()

    user_answer_correct = is_correct(user_choice, item_a, item_b)

    if user_answer_correct:
        score += 1
        print(f"You are correct! New score: {score}")
        print("\n" * 20)
    else:
        print(f"That's wrong. Final score: {score}")
        game_over = True



""" What I've learned on Day 14:

1. item_b should've been outside of the loop. At the very beginning of the loop, we assign the value of item_b
 to item_a. Then, we we assign a random choice to item_b. This way, upon every iteration, the value of whatever item?b
 was, will be used for item_a. 
 
 2. I could've used random.choice(data) on the list instead of saving doing random_choice_a = random.randint(0, length
 of list -1) to get one object. 
 
 3. If item_a and item_b are equal, I can easily assign a new random choice to item_b before continuing.
 
 4. As long as users don't type the letters I requested, they're stuck in an eternal loop.
 
 5. To check the correct user choice, a function prevents repeating code. First we check which account has the
 most followers. Then if the user's choice resembles this, and return true or false. We don't JUST call the function.
 We also save the value in a new variable to print the score or determine the game's over. 
 
 6. You can't 'just' refer to the function call is_correct, and then do nothing else with it (not call it). It will
 always be 'truthy' therefore whatever users type, the answer will be correct. """
