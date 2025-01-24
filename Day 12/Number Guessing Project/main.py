from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")

def play_game():
    game_over = False
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10
    # number_to_guess = 35  # for testing purposes
    number_to_guess = random.randint(1,100)
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while not game_over and attempts > 0:
        print(f"You have {attempts} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You've guessed {number_to_guess} correctly! Refresh the page to play again.")
            game_over = True
            attempts = 0
        elif guess < number_to_guess:
            print("Too low. ")
            attempts -= 1
            if attempts == 0:
                game_over = True
                print("You've run out of guesses. Refresh the page to play again.")
            else:
                print("Guess again.")
        else:
            print("Too high. Guess again")
            attempts -= 1
            if attempts == 0:
                game_over = True
                print("You've run out of guesses. Refresh the page to play again.")
            else:
                print("Guess again.")

play_game()