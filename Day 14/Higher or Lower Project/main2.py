from art import logo, vs
from game_data import data # 50 items
import random
import os

score = 0
game_over = False # when game over, end ongoing loop with new comparisons

print(logo)

list_length = len(data)

def get_random_number():
    random_number = random.randint(0, list_length - 1)
    return random_number

position_a = random.randint(0, list_length - 1)  # -1 to correct for randint stop
position_b = random.randint(0, list_length - 1)

print(f"Compare A: {data[position_a]['name']}, a {data[position_a]['description']} from {data[position_a]['country']}")
print(vs)  # https://www.geeksforgeeks.org/how-to-access-dict-attribute-in-python/
print(f"Against B: {data[position_b]['name']}, a {data[position_b]['description']} from {data[position_b]['country']}")

while not game_over:
    new_index_a = 0
    new_index_b = 0

    user_choice = input("Who has more followers? Type 'A' or 'B'").upper()
    options = ["A", "B"]
    while not user_choice in options:
        user_choice = input("Who has more followers? Type 'A' or 'B'").upper()

    if user_choice == "A":
        if data[position_a]['follower_count'] > data[position_b]['follower_count']:
            score += 1
            print(f"You are correct! Score: {score}")
            # clear console
            print(logo)
            new_index_a = position_b
            print(f"Compare A: {data[new_index_a]['name']}, a {data[new_index_a]['description']} from {data[new_index_a]['country']}")
            print(vs)
            new_index_b = get_random_number()
            print(f"The object at index {new_index_b} is {data[new_index_b]}")
            print(f"Against B: {data[new_index_b]['name']}, a {data[new_index_b]['description']} from {data[new_index_b]['country']}")
        else:
            print(f"You lose! Score: {score}")
            game_over = True
    else: # user_choice = "B"
        if data[position_b]['follower_count'] > data[position_a]['follower_count']:
            score += 1
            print(f"You are correct! Score: {score}")
            # a_random_choice becomes this entry
        else:
            print(f"You lose! Score: {score}")
            game_over = True



# ONCE CORRECt, B  becomes the A choice in the next iteration.
#clear console each time
# nice to have: indices can't be the same