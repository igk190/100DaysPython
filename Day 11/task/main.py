import random
import art

def deal_card(): # hint 4
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(list):  # hint 6, 7
    """Calculate total score of cards inside a list"""
    if len(list) == 2:
        if sum(list) == 21:
            return 0 # blackjack
        else:
            return sum(list)
    elif 11 in list: # hint 8
        if sum(list) > 21:
            list.remove(11)
            list.append(1)
            print(f"LIST AFTER 11: {list}")
            return sum(list)
        else:
            return sum(list)
    else:
        return sum(list)

def compare(user_score, computer_score):
    if computer_score == user_score: # draw
        return "It's a draw!😮\n"
    elif user_score == 0 or computer_score == 0: # hint 9 / blackjacks
        if computer_score == 0:
            return "\nYou lose😢\n"
        else:
            return "You win! WOW\n"
    elif user_score > 21:
        return "You went over. You lose!\n"
    elif computer_score > 21: # user highest score
        return "Computer went over. You win!!!\n"
    # why it prints nothing when I use print statements instead of return?

def play_game():
    print(art.logo)

    user_cards = []
    user_score = 0
    computer_cards = []
    computer_score = 0
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}. Current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score > 21 or computer_score > 21:
            game_over = True
        else:
            draw_new_card = input("Do you want to draw another card? 'y' or 'n'\n")  # hint 10
            if draw_new_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score,computer_score))
    print(f"\nYour final hand: {user_cards}, Your final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, computer final score: {computer_score}\n")

while input("Do you want to play a Blackjack game? Type 'y' or 'n'") == "y":
    print("\n" * 20)
    play_game()


