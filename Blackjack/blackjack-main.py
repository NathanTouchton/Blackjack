############### Blackjack Project #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import os
def clear():
    os.system('clear')

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    card = random.choice(cards)
    return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(card_list):
    score = sum(card_list)
    if card_list == [11, 10] or card_list == [10, 11]:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return score
    
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
# done
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
# done
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

computer_score = calculate_score(computer_cards)
user_score = calculate_score(user_cards)

def game():
    user_score = calculate_score(user_cards)
    print(user_score)
    if user_score == 0 or computer_score == 0:
        return
    elif user_score > 21:
        return
    else:
        user_continue_choice = input("Do you want to draw another card? Type 'y' for yes and 'n' for no.").lower()
        if user_continue_choice == "n":
            return
        elif user_continue_choice == "y":
            user_cards.append(deal_card())
        game()

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
# done
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
# done
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
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

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

game()
compare(user_score, computer_score)
