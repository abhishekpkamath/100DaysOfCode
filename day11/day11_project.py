############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def decide_winner(user_score, computer_score):
    if user_score == computer_score:
        print("Draw!")
    elif user_score == 21:
        print("User BlackJack, You win!")
    elif computer_score == 21:
        print("Computer BlackJack, You lose!")
    elif user_score > 21:
        print("You went over, you lose!")
    elif computer_score > 21:
        print("Dealer went over, You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")       


def generate_computer_deck(computer_deck, computer_score):
    while computer_score < 17:
        computer_deck.append(random.choice(cards))
        computer_score = sum(computer_deck)
    return computer_deck, computer_score


def generate_user_deck(user_deck, user_score):
    new_card = random.choice(cards)
    if new_card == 11 and (user_score + new_card) > 21:
        new_card = 1
    user_deck.append(new_card)
    user_score = sum(user_deck)
    return user_deck, user_score


def show_scores(user_deck, user_score, computer_deck):
    print(f"\tYour cards: {user_deck}, current_score: {user_score}")
    print(f"\tComputer's first card: {computer_deck[0]}")


def blackjack():
    print(logo)
    user_deck = [random.choice(cards), random.choice(cards)]
    user_score = sum(user_deck)
    computer_deck = [random.choice(cards)]
    computer_score = sum(computer_deck)
    show_scores(user_deck, user_score, computer_deck)
    if user_score != 21:
        while user_score <= 21 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            user_deck, user_score = generate_user_deck(user_deck, user_score)
            show_scores(user_deck, user_score, computer_deck)  
    computer_deck, computer_score = generate_computer_deck(computer_deck, computer_score)
    print(f"Your final hand: {user_deck}, final score: {user_score}")
    print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")
    decide_winner(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()