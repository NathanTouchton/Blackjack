# Blackjack project
# cards = [11, 2, 3, 4, 5, 6, 7, 8]

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import os
def clear():
    os.system('clear')

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    score = sum(card_list)
    if card_list == [11, 10] or card_list == [10, 11]:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return score
def game():
    user_score = calculate_score(user_cards)
    print(user_score)
    if user_score == 0 or computer_score == 0:
        return
    elif user_score > 21:
        return
    else:
        user_continue_choice = input("Do you want to draw another card? Type 'y' for yes and 'n' for no. ").lower()
        if user_continue_choice == "n":
            return
        elif user_continue_choice == "y":
            user_cards.append(deal_card())
        game()
def compare(user_score_function, computer_score_function):
    if user_score_function == computer_score_function:
        print(f"It's a draw! Your score is {user_score_function}. Game over!")
    elif computer_score_function == 0:
        print(f"You lose! The dealer got a blackjack. Your score is {user_score_function} Game over!")
    elif user_score_function == 0:
        print(f"You Win! You got a blackjack. The dealer's score is {computer_score_function}. Game over!")
    elif user_score_function > 21:
        print(f"You lose! Your score is {user_score_function}, which is greater than 21. Game over!")
    elif computer_score_function > 21:
        print(f"You win! Your score is {user_score_function}, and the dealer's score is {computer_score_function}. Game over!")
    else:
        if user_score_function > computer_score_function:
            print(f"You win! Your score is {user_score_function}, and the dealer's score is {computer_score_function}. Game over!")
        elif computer_score_function > user_score_function:
            print(f"You lose! Your score is {user_score_function}, and the dealer's score is {computer_score_function}. Game over!")
user_cards = []
computer_cards = []
def deal_cards_new_game():
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

deal_cards_new_game()
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

game()
compare(user_score, computer_score)

restart_input = input("Would you like to restart? Type 'y' for yes and 'n' for no. ").lower()
if restart_input == "y":
    clear()
    user_cards = []
    computer_cards = []
    deal_cards_new_game()
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    game()
    compare(user_score, computer_score)
else:
    clear()
    print("Thank you for playing!")