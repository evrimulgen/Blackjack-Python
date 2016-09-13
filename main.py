from cards import *
from sys import exit

DECK_LENGTH = 52
SUITS = 'cdhs'
RANKS = '23456789TJQKA'

def playGame():
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


playAgain = 1
while(playAgain):
	playGame()
	playAgain = raw_input("Play Again? (1/0): ")
	
