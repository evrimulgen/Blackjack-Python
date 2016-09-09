import random
import itertools

def rank(card):
    return card[0]
def suit(card):
    if (card[1] == 'c'):
        return "clubs"
    elif (card[1] == 's'):
        return "spades"
    elif (card[1] == 'h'):
        return "hearts"
    elif (card[1] == 'd'):
        return "diamonds"
    else:
        return "NULL"

def card(card):
    return (rank(card) + " of " + suit(card))

def value(card):
    if (card[0].isalpha()) and (card[0] != 'A'):
        return 10
    elif (card[0] == 'A'):
        return 11
    else:
        return int(card[0])

def handValue(hand):
    total = 0
    for index in range(len(hand)):
        total = total + value(hand[index])
    return total

def displayHands(playerHand, dealerHand):
    print("\nYour cards:")
    for index in range(len(playerHand)):
        print(card(playerHand[index]))
    print("Total: " + str(handValue(playerHand)))

    print("\nDealer's card:")
    print(card(dealerHand[0]))
    for index in range(len(card(dealerHand[0])) / 2):
        print("-"),
    print("\n")


def clearScreen():
    for i in range(100):
        print("\n")

def menu():
    raw_input("PRESS ENTER TO START")
    clearScreen()
    return
