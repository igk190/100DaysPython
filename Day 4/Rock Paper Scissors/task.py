import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
pc_hand = random.randint(0,2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

game_options = [0,1,2,]
if user_choice not in game_options:
    print("Wrong choice, you lose!")

print(f"You chose: {game_images[user_choice]}")
print(f"PC chose: \n{game_images[pc_hand]}")

if user_choice == pc_hand:
    print("It's a draw!")
elif user_choice == 0 and pc_hand == 2:
    print("You win!")
elif pc_hand == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > pc_hand:
    print("You win!")
elif  pc_hand > user_choice:
    print("You lose!")