from cards import *
import sys
import os

DECK_LENGTH = 52
SUITS = 'cdhs'
RANKS = '23456789TJQKA'
deck = list(''.join(card) for card in itertools.product(RANKS, SUITS))
random.shuffle(deck)

playerHand = [deck.pop(), deck.pop()]
dealerHand = [deck.pop(), deck.pop()]

clearScreen()
displayHands(playerHand, dealerHand)
if(isBlackJack(playerHand)):
	print("PLAYER WINS WITH BLACKJACK!")
	raw_input("Press Enter to Continue")
	exit()
# TODO: Check for Ace value (1 or 11)
playerChoice = raw_input("(h)it or (s)stand?: ")
while (playerChoice == 'h'):
        print("hit!")
        playerHand.append(deck.pop())
        displayHands(playerHand, dealerHand)
        playerChoice = raw_input("(h)it or (s)stand?: ")

print("stand!")
while(handValue(dealerHand) <= 16):
    dealerHand.append(deck.pop())
playerTotal = handValue(playerHand)
dealerTotal = handValue(dealerHand)
print("Player Total: " + str(playerTotal))
print("Dealer Total: " + str(dealerTotal))
if(playerTotal > dealerTotal) and (playerTotal <= 21):
    print("PLAYER WINS")
else:
    print("PLAYER LOSES")
raw_input("Press Any key to Continue")
