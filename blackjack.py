import random
cards = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
suits = ['Hearts','Diamonds','Spades','Clubs']
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.facedown = False
        self.value = 0
    def __repr__(self):
        if self.facedown == True:
            return str('?')
        if self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
            self.value = 10
        elif self.rank == 'Ace':
            self.value = 1
        else:
            self.value = self.rank
            
        return str(self.rank) + " " + str(self.suit)
        
class Deck:
    def __init__(self,num_decks = 2):
        self.cards = []
        for amt in range(num_decks):
            for card in cards:
                for suit in suits:
                    card_ = Card(card,suit)
                    self.cards.append(card_)

        random.shuffle(self.cards)
    def __repr__(self):
        return str(self.cards)
    def drawTopCard(self):
        return self.cards.pop()
        
deck = Deck()
player = []
dealer = []
playerTotal = 0
while len(player) <2:
    tempCard = deck.drawTopCard()
    player.append(tempCard)
while len(dealer) <2:
    tempCard = deck.drawTopCard()
    dealer.append(tempCard)
dealer[1].facedown = True
print(player)
print(dealer)

if player[0].rank == 'Ace' and player[1].value == 10:
    if dealer[0].rank == 'Ace' and dealer[1].value == 10:
        print("Tie")
    else:
        print("Player Wins")
elif dealer[0].rank == 'Ace' and dealer[1].value == 10:
    print("Dealer Wins")
while True:
    choice = input("Stand or hit?").lower()
    if choice == "stand":
        break
    elif choice == "hit":
        tempCard = deck.drawTopCard()
        player.append(tempCard)
        for card in player:
            if card == 'Ace':
                break
            else:
                playerTotal += card.value
        if playerTotal >21:
            print("Pkotpdk")
            break
    else:
        continue   

    if playerTotal == 21:
        print("Player wins")



        
