#This is the code that was provided via Canvas.
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)


#clearDeck sets all of the locations of the cards back to 0 (the deck)
#This is not really relevant to the main project but could be used in the black belt.
def clearDeck():
    for i in range(NUMCARDS):
        cardLoc[i] = 0
      
#assignCard chooses a random index from 0-51 and depending on which variable
#is passed through, will store that card in the appropriate "hand"
def assignCard(Player):
    keepgoing = True
    #by using a while loop you are able to control that it continually chooses
    #a random number until my condition is satisfied.
    while keepgoing:
        x = randrange(0,51)
        if cardLoc[x] != 0:
            x = randrange(0,51)
        else:
            keepgoing = False
        cardLoc[x] = Player
    return Player

#showDeck is going to display every card, its index in cardLoc and what "hand" it's in
def showDeck():
    for i in range(NUMCARDS):
        #I made all of the following variables to make it easier to use the
        #print statement coming up.
        z = cardLoc[i]
        a = i%13
        b = int(i/13)
        #this code will display the indexes of all of the cards
        print("{0:<10} {1:<2} of {2:<10} {3:<5}".format(i, rankName[a], suitName[b], playerName[z]))
    #creates space between the list of cards and player's cards
    print("\n")

#The showHand function shows what cards are in both the player and computer's hand.
def showHand(Player):
    if Player == 1:
      print("PLAYER CARDS:")
    else:
      print("COMPUTER CARDS:")
#The for loop finds the value it is looking for (either 1 or 2), notes the cared,
#and stores it appropriately so that it is visible when displaying the hands.
    for i in range(5):
        x = cardLoc.index(Player)
        a = x%13
        b = int(x/13)
        print("{} of {}".format(rankName[a], suitName[b]))
        cardLoc[x] = 0
    #creates space between the player's card list and the computer's cards
    print("\n")
        
main()
