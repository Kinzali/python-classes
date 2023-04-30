# LUO TAI MUOKKAA OHJELMAA NIIN, ETTÄ ON 2 LUOKKAA: DECK JA CARD.
# KATSO CARD-LUOKASTA MALLIA EDELTÄVÄSTÄ DECK-HARJOITUKSESTA.
# MUUTA KOODIA NIIN, ETTÄ DECK-LUOKAN KONSTRUKTORISSA TEHDÄÄN Tk-LUOKASTA OLIO
# JA KUTSUTAAN:
# - self.fill_deck()
# - self.deal()
# - self.win.mainloop()

# DEAL-METODISSA, LISÄÄ BUTTONIT(KORTIT)gridiin.

# CARD-LUOKAN KONSTRUKTORISSA, HAE KORTIN KUVA, 
# MUUTA PHOTOIMAGEKSI JA SUURENNA KUVA
# JA LUO KYSEISESTÄ KORTISTA BUTTON, JOKA SAA KUVAKSEEN KYSEISEN KORTTIKUVAN.
# BUTTONIA PAINETTASSA TULEE KUTSUA CARD-LUOKAN CHANGE_CARD-METODIA, JOKA MUUTTAA
# KORTIN KUVAN JOKSIKIN TOISEKSI.

from tkinter import *
import os
import random

from PIL import Image, ImageTk

class Deck:
    def __init__(self):
        self.win= Tk()        
        self.cards = []
        self.fill_deck()
        self.deal()
        self.win.mainloop()
        
    def fill_deck(self):
        suit = 1
        value= 1
        while suit < 4:
            value = 1
            while value < 13:
                card = Card(suit,value)
                self.cards.append(card)
                value += 1
            suit += 1
             # for card in self.cards:
        #print(card.suit, card.value)
        random.shuffle(self.cards)
   
        
    def deal(self):
        index = 0
        for row in range(1,4):
            for column in range(0,13):
                self.cards[index].Button.grid(row=row, column=column -1)
                index += 1
                       
            
class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        self.image = ImageTk.PhotoImage(Image.open(os.getcwd()+"/cards/"+str(value)+"_"+str(value)+".png"))
        self.back= ImageTk.PhotoImage(Image.open(os.getcwd()+"/cards/cards_back.png").resize((128,128)))
        self.Button = Button(image=self.image,  command=lambda:self.show_card(self))
        
    def change_card(self):        
        self.changed_image = ImageTk.PhotoImage(Image.open(os.getcwd()+'/cards_p2/spade_1.png').resize((128,128))) # pisteellä voi myös viitata nykyiseen hakemistoon
    # configurella voi muuttaa samoja asetuksia, jotka Button-luokan oliota tehdessä voi asettaa

    def show_card(self):
        self.button.configure(image=self.image)
        
    def click(self,num):
        #kun korttia painaa, muuttuu sen kuva 1_1.png:ksi
        self.buttons[num].configure(image=self.images[0])
        
deck = Deck()
