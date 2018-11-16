from random import randint
from random import shuffle
import webbrowser
import time

class cards: #Defining the class for all cards
    def __init__(self, color, value, name):
        self.color = color
        self.value = value
        self.name = name

# creating the class 'player'. Boolean 'isBank' is used for different behaviors for Bank and Player. Also Booleans to
#  check for BlackJack and Triple Seven
class player:
    def __init__(self, budget, hand, currentHandValue, numberOfCardsDealt, isBank, hasPlayerBusted, hasBlackJack, hasTripleSeven, hasPlayerWonRound, numberOfAces):
        self.isBank = isBank
        self.budget = budget
        self.hand = hand
        self.currentHandValue = currentHandValue
        self.numberOfAces = numberOfAces
        self.hasPlayerBusted = hasPlayerBusted
        self.hasBlackJack = hasBlackJack
        self.hasTripleSeven = hasTripleSeven
        self.numberOfCardsDealt = numberOfCardsDealt
        self.hasPlayerWonRound = hasPlayerWonRound

def placeBet(player): # Function in order to make the player place a bet and return the new budget of the player
    x = player.budget
    bet = int(input("Place your Bet: \n \n"))
    while bet < 25:
        bet = int(input("You have to bet at least 25 CHF! Place again: "))
    while bet > x:
        print("You can not bet more than your current budget:", player.budget, "- Try Again!")
        bet = int(input())

    player.budget = x - bet
    return bet

#function that lets the player hit another card or choose to stay with the current hand. It will also check
def hitOrStand(player, deck):

    # behavior for Bank: This is the standard casino policy: If Bank's hand is <17, it will automatically hit, even if
    # this means an automatic loss for the bank. This is done in order to prevent the Bank to play irrationally
        if player.isBank == True:
            while player.currentHandValue < 17:
                dealCard(1,player,deck)

        #behavior for human player. When currentHandValue is > 21 the function is  stopped as player automatically lost
        else:
            hit = True
            while hit is True:
                if player.currentHandValue > 21:
                    hit = False
                if hit is True:
                    decision = input("Do you want to hit or stand? \n \n")
                    if decision == "stand" or decision is "Stand" or decision is "S":
                        hit = False
                    elif decision == "hit" or decision == "Hit" or decision == "H":
                        dealCard(1,player,deck)
                        print("Your Hand: ", end='')
                        for n in range(player1.numberOfCardsDealt):
                            print(player1.hand[n].name, "| ", end='')
                        print(" Value:", player1.currentHandValue)
                    else:
                        hit = False

        if player.currentHandValue > 21:
            player.hasPlayerBusted = True
        else:
            player.hasPlayerBusted = False
        return player

def checkForBust(player): #function to check if player has Busted
    if player.currentHandValue > 21:
        player.hasPlayerBusted = True
    else:
        player.hasPlayerBusted = False
    return player.hasPlayerBusted

def checkForBlackjack(player): #function to check if Player has a BlackJack OR a Triple Seven.
    if player.hand[0].value + player.hand[1].value == 21 and player.numberOfAces > 0:
        player.hasBlackJack = True

    if player.hand[0].value == 7 and player1.hand[1].value == 7 and player.hand[2].value == 7:
        player.hasTripleSeven = True

def newRound(a,b):
    a.currentHandValue = 0
    b.currentHandValue = 0
    a.hasBlackJack = False
    b.hasBlackJack = False
    a.hasTripleSeven = False
    b.hasTripleSeven = False
    a.hasPlayerWonRound = False
    b.hasPlayerWonRound = False
    a.hasPlayerBusted = False
    b.hasPlayerBusted = False
    a.hand.clear()
    b.hand.clear()
    a.numberOfAces = 0
    b.numberOfAces = 0
    a.numberOfCardsDealt = 0
    b.numberOfCardsDealt = 0

    #resets all values for new round such as currenHandValue, but also shuffling a new deck
    pass

#function the Winner is determined by bool player.hasPlayerWonRound
def whoWonRound(playera,playerb):

    #First, check if any of the Players has Busted
    if playera.hasPlayerBusted == True:
        bank.hasPlayerWonRound = True
    elif playerb.hasPlayerBusted == True:
        playera.hasPlayerWonRound = True

    #Second, check if any of the Players have A triple Seven, as Triple Seven beats BlackJack and leads to automatic win
    # for human Player
    if playera.hasPlayerWonRound == False and playerb.hasPlayerWonRound == False:
        if playera.hasTripleSeven == True:
            playera.hasPlayerWonRound = True
        if playerb.hasTripleSeven == True:
            playerb.hasPlayerWonRound = True

    #Now, BlackJack gets Checked.
        if playera.hasTripleSeven == False and playerb.hasTripleSeven == False:
            if playera.hasBlackJack == True:
                playera.hasPlayerWonRound = True
        if playerb.hasBlackJack == True:
            playerb.hasBlackJack = True

    #Lastly, if no one has a BlackJack or triple Seven, the Hand Values get checked
        if playera.hasBlackJack == False and playerb.hasBlackJack == False and playera.hasTripleSeven == False and playerb.hasTripleSeven == False:
            if playera.currentHandValue > playerb.currentHandValue:
                playera.hasPlayerWonRound = True
            elif playera.currentHandValue < playerb.currentHandValue:
                playerb.hasPlayerWonRound = True
            else:
                playera.hasPlayerWonRound = True
                playerb.hasPlayerWonRound = True

def payRound(playera,playerb, b): #function to pay out after end of round where b is the bet placed by player 1


    if playera.hasTripleSeven == True:
        playera.budget += b * 3 / 2

    elif playera.hasBlackJack == True and playerb.hasBlackJack == False:
        playera.budget += b * 3 / 2

    elif playera.hasTripleSeven == False and playera.hasBlackJack == False and playera.hasPlayerWonRound== True and playerb.hasPlayerWonRound == False:
        playera.budget += b * 2

    elif playera.hasTripleSeven == False and playera.hasBlackJack == False and playera.hasPlayerWonRound== True and playerb.hasPlayerWonRound == True:
        playera.budget += b

def dealCard(nOfCards,player, deck): #function that deals cards for the players. Pop() removes the dealt card to prevent double cards
    for n in range(nOfCards):
        shuffle(deck)
        player.hand.append(deck.pop())
        player.currentHandValue += player.hand[-1].value
        #check if the last Dealt hand was an Ace
        if player.hand[-1].value == 11:
            player.numberOfAces += 1
        #check if the players current Hand is above 21 and contains Aces. This makes Aces count as 1 instead of 11
        while player.currentHandValue > 21 and player.numberOfAces > 0:
            player.currentHandValue -= 10
            player.numberOfAces -= 1

        n += 1
    player.numberOfCardsDealt += nOfCards
    return deck

def buildDeck(deck): # Function to build the deck
    deck.clear()
    for i in range(2, 11):
        t = True
        g = True
        while t == True:
            deck.append(cards('Hearts', i, str(i) + " of " + "Hearts"))
            deck.append(cards('Diamonds', i, str(i) + " of " + "Diamonds"))
            deck.append(cards('Spades,', i, str(i) + " of " + "Spades"))
            deck.append(cards('Crosses', i, str(i) + " of " + "Crosses"))
            t = False

        if i == 10:
            for b in range(3):
                deck.append(cards('Hearts', 10, faceCards[b] + " of " + "Hearts"))
                deck.append(cards('Diamonds', 10, faceCards[b] + " of " + "Diamonds"))
                deck.append(cards('Spades', 10, faceCards[b] + " of " + "Spades"))
                deck.append(cards('Crosses', 10, faceCards[b] + " of " + "Crosses"))

            while g == True:
                deck.append(cards('Hearts', 11, faceCards[3] + " of " + "Hearts"))
                deck.append(cards('Diamonds', 11, faceCards[3] + " of " + "Diamonds"))
                deck.append(cards('Spades', 11, faceCards[3] + " of " + "Spades"))
                deck.append(cards('Crosses', 11, faceCards[3] + " of " + "Crosses"))
                g = False
    return deck

hasGameEnded = False
faceCards = ['Jack', 'Queen', 'King', 'Ace']
card_deck = []
print("Let us start playing!")
player1 = player(5000, [], 0, 0, False, False, False, False, False, 0)
bank = player(100000000,[], 0, 0, True, False, False, False, False, 0)

#start of the actual game
while hasGameEnded == False:
    print("\n"* 1)
    print( " -------New Round-------")

    ##resetting all values for new rounds and shuffling a new deck
    stand = False
    newRound(player1, bank)
    card_deck = buildDeck(card_deck)

    #Placing a bet
    currentBet = placeBet(player1)

    #start dealing the hands
    dealCard(2,player1,card_deck)
    dealCard(2,bank, card_deck)

    #Printing the Hand of the Players
    print("Your Hand: ", end='')
    for n in range(player1.numberOfCardsDealt):
        print(player1.hand[n].name, "| ", end='')
    print(" Value:", player1.currentHandValue)
    print("The Banks Hand: ", end='' )
    for n in range(bank.numberOfCardsDealt):
        print(bank.hand[n].name, "| ", end='')
    print(" Value:", bank.currentHandValue)

    #Let Player Hit or Stand their Current card and Check if their new hand is above 21
    player1.hasPlayerBusted = hitOrStand(player1, card_deck)
    player1.hasPlayerBusted = checkForBust(player1)
    if player1.hasPlayerBusted == True:
        print("Unfortunately, you busted!")
    else:
        hitOrStand(bank,card_deck)
        checkForBust(bank)
        if bank.hasPlayerBusted== True:
            print("The bank lost, lucky you!")

    #Check For Blackjack or Triple Seven for Player and Bank
    checkForBlackjack(player1)
    checkForBlackjack(bank)

    #Check if the Player has Won the round and pay the current bet
    whoWonRound(player1,bank)
    payRound(player1, bank, currentBet)

    #Printing the Final Hands
    print("Final Hands: ")
    print("Hand of Player 1: ", player1.currentHandValue)
    print("Hand of Bank: ", bank.currentHandValue)
    if player1.hasBlackJack == True:
        print("You got a BLACKJACK!!")
    if bank.hasBlackJack == True:
        print("The Bank has a BLACKJACK!")
    if player1.hasTripleSeven == True:
        print("TRIPLE SEVEN! You win")
    if bank.hasTripleSeven == True:
        print("The Bank has a TRIPLE SEVEN!!")
    time.sleep(4)
    print("\n"*30)
    print("Your current budget: ", player1.budget)

    if player1.budget > 25:
        decision = input("Type 'C' to Cash Out, Press Enter to keep Playing \n \n ")
        if decision == 'C' or decision == 'c':
            hasGameEnded = True
    if player1.budget < 25:
        hasGameEnded = True
    print("\n"*30)

if player1.budget < 25:
    webbrowser.open('https://www.youtube.com/watch?v=Q2jnF1pOHyw')

if player1.budget > 20000:
    webbrowser.open('http://www.youtube.com/watch?v=T9Op2YQ7yyU&t=1m21s')


