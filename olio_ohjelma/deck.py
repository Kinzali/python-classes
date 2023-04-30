class Deck:
    def __init__(self):
        self.cards = []
        self.fill_deck()
        self.deal()

    def fill_deck(self):
        for i in range(1,14):
            card = Card('spade', i)
            self.cards.append(card)
            #self.cards.append(Card('spade',i))

    def deal(self):
        # for i in range(len(self.cards)):
        #     print(self.cards[i].suit, self.cards[i].value)
        # tai lyhyemmin
        for i in self.cards:
            print(i.suit, i.value)

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

deck = Deck()
