import random

# possible cards
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']

# dealers' cards
dealer_cards = []

# player's cards
player_cards = []

# deal cards
while len(player_cards) != 2:
    player_cards.append(random.choice(cards))
    if len(player_cards) == 2:
        print("Your cards are: ", player_cards[0] + " & " + player_cards[1])

# Dealer's cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.choice(cards))
    if len(dealer_cards) == 2:
        print("Dealers cards are: X &", dealer_cards[1])

# Actions
dealerCard1 = 0
dealerCard2 = 0
playerCard1 = 0
playerCard2 = 0


def changeToInt(ace):
    global dealerCard1
    try:
        dealerCard1 = int(dealer_cards[0])
    except ValueError:
        if dealer_cards[0] == 'A':
            dealerCard1 = ace
        else:
            dealerCard1 = 10
    global dealerCard2
    try:
        dealerCard2 = int(dealer_cards[1])
    except ValueError:
        if dealer_cards[1] == 'A':
            dealerCard2 = ace
        else:
            dealerCard2 = 10
    global playerCard1
    try:
        playerCard1 = int(player_cards[0])
    except ValueError:
        if player_cards[0] == 'A':
            playerCard1 = ace
        else:
            playerCard1 = 10
    global playerCard2
    try:
        playerCard2 = int(player_cards[1])
    except ValueError:
        if player_cards[1] == 'A':
            playerCard2 = ace
        else:
            playerCard2 = 10


playerAddedInt = 0
playerNextCard = 0

def changeNextPlayerCard(ace):
    global playerAddedInt
    global playerNextCard
    try:
        playerAddedInt = int(playerNextCard)
    except ValueError:
        if playerNextCard == 'A':
            playerAddedInt = ace
        else:
            playerAddedInt = 10


changeToInt(11)
dealerCardSum = dealerCard1 + dealerCard2
playerCardSum = playerCard1 + playerCard2


def actionFunction(aceNum):
    global playerCardSum
    global dealerCardSum
    global playerNextCard
    stayOrHit = 0

    while stayOrHit == 0:
        action = str(input("Please type 'stay' to stay and 'hit' to hit "))
        if action == 'hit':
            playerNextCard = random.choice(cards)
            print("Your new card is", playerNextCard)
            changeNextPlayerCard(aceNum)
            playerCardSum += playerAddedInt
            print("Your new total sum is", playerCardSum)
            if playerCardSum > 21:
                print("You lost!")
        elif action == 'stay':
            stayOrHit = 1

    print("Dealers cards are", dealer_cards[0], dealer_cards[1])

    while dealerCardSum < playerCardSum & playerCardSum < 22:
        dealerNextCard = random.choice(cards)
        print("Dealer's next card is", dealerNextCard)
        try:
            dealerAddedInt = int(dealerNextCard)
        except ValueError:
            if dealerNextCard == 'A':
                dealerAddedInt = 11
            else:
                dealerAddedInt = 10
        dealerCardSum += dealerAddedInt
        print("The Dealer's total sum is ", dealerCardSum)
        if dealerCardSum > 21:
            print("Dealer busted, you win!")
            exit()
        elif dealerCardSum == 21:
            if playerCardSum == 21:
                print("You both got blackjack, no one won!")
                exit()
            elif playerCardSum < 21:
                print("The dealer got blackjack. You lost!")
                exit()

    if dealerCardSum > playerCardSum & dealerCardSum < 21 & playerCardSum < 22:
        print("Dealer has ", dealerCardSum, " while you have ", playerCardSum, ", so dealer wins!")
        exit()
    elif playerCardSum > 22:
        print("Dealer has ", dealerCardSum, " while you have ", playerCardSum, ", so dealer wins!")
        exit()
    elif playerCardSum == dealerCardSum:
        print("You and the Dealer tied, so no one won!")
        exit()


actionFunction(11)