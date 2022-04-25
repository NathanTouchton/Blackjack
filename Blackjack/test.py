cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
cards_dictionary = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": cards[9],
    "Jack": cards[10],
    "Queen": cards[11],
    "King": cards[12],
}
user_cards = []
def deal_card():
    card = random.choice(cards)
    return card
def display_hand():
    print(cards_dictionary[user_cards])

user_cards.append(deal_card())
user_cards.append(deal_card())

display_hand()