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

    # Checks for Aces in hand, if card == 'A', total is reduced by 10.
    # If multiple Aces, then it checks if the hand is currently under 21.
    # If it is, we just break because the score is already valid and does not need further reduction.
    if (total > 21):
        for index in range(len(hand)):
            if(hand[index][0] == 'A'):
                total -= 10
            if(total <= 21):
                break
            else:
                continue

    return total

def displayHands(playerHand, dealerHand, showDealerCardsFlag):
    # showDealerCardsFlag: True to show all cards, false otherwise
    print("\nYour cards:")
    for index in range(len(playerHand)):
        print(card(playerHand[index]))
    print("Total: " + str(handValue(playerHand)))

    if(showDealerCardsFlag == True):
        print("\nDealer's cards:")
        for index in range(len(dealerHand)):
            print(card(dealerHand[index]))
        print("Total: " + str(handValue(dealerHand)))
    else:
        print("\nDealer's card:")
        print(card(dealerHand[0]))
        for index in range(len(card(dealerHand[0])) / 2):
            print("-"),
        print("\n")

def isBlackJack(playerHand):
	if(rank(playerHand[0]) == 'A'):
		if(rank(playerHand[1]) == 'K') or (rank(playerHand[1]) == 'Q') or (rank(playerHand[1]) == 'J'):
			return 1
	elif(rank(playerHand[1]) == 'A'):
		if(rank(playerHand[0]) == 'K') or (rank(playerHand[0]) == 'Q') or (rank(playerHand[0]) == 'J'):
			return 1
	else:
		return 0

def advice(playerHand):
    playerTotal = handValue(playerHand)
    if(playerTotal <= 16): return "HIT (under 16)"
    else: return "STAND (over 16)"

def bustChance(playerHand):
    playerTotal = handValue(playerHand)
    if(playerTotal == 12):
        return "31"
    elif(playerTotal == 13):
        return "39"
    elif(playerTotal == 14):
        return "56"
    elif(playerTotal == 15):
        return "58"
    elif(playerTotal == 16):
        return "62"
    elif(playerTotal == 17):
        return "69"
    elif(playerTotal == 18):
        return "77"
    elif(playerTotal == 19):
        return "85"
    elif(playerTotal == 20):
        return "92"
    else:
        return "Less than 30"

			
def clearScreen():
    for i in range(100):
        print("\n")

def menu():
    raw_input("PRESS ENTER TO START")
    clearScreen()
    return
