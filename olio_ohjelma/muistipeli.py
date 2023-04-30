from tkinter import *
from PIL import Image, ImageTk
import random

class Deck():
    def __init__(self):
        self.win=Tk()
        self.cards=[]
        self.chosen1 = None
        self.chosen2 = None
        self.fill_deck()
        self.deal()
        self.win.mainloop()

    def fill_deck(self): #täyttäisi self.cards:it card-luokan olioilla
        suit = 1
        value = 1
        while suit < 5:
            value = 1
            while value < 14:
                card = Card(suit,value, self)
                self.cards.append(card)
                value += 1
            suit += 1        
        # for card in self.cards:
        #     print (card.suit, card.value)                                
        #random.shuffle(self.cards)

    def deal(self):
        # 2 sisäkkäistä loopia, jotta kortit saadaan näkymään gridissä
        index = 0
        for row in range(1,5): # 1-4
            for column in range(1,14):
                self.cards[index].button.grid(row=row, column=column-1)
                index += 1

    def choose_card(self,card):  
        if self.chosen1==None: #1.korttia ei ole valittu
            self.chosen1 = card # asetetaan 1.kortiksi kyseinen kortti
            card.button.configure(image=card.image) #käännetään kortin maa ja value näkyviin
        elif self.chosen2==None:
            self.chosen2=card
            card.button.configure(image=card.image)
            # tässä vaiheessa tarkistetaan kuvien valuet
            self.check_cards()

    def check_cards(self):        
        if self.chosen1.value == self.chosen2.value:
            self.chosen1.button["state"]=DISABLED
            self.chosen2.button["state"]=DISABLED
            #asetetaan valitut kortit None-tilaan, jotta voidaan valita uusia kortteja
            self.chosen1 = None
            self.chosen2 = None
        else:     #after=mitä metodia kutsutaan tietyn ajan jälkeen(millisec,func)
            self.win.after(1000, self.reset_cards) 

    def reset_cards(self):
        self.chosen1.button.configure(image=self.chosen1.back)
        self.chosen2.button.configure(image=self.chosen2.back)
        self.chosen1 = None
        self.chosen2 = None

#region commented
        # if card.current_image == card.back:
        #     card.button.configure(image=card.image)
        #     card.current_image = card.image
        # else:
        #     card.button.configure(image=card.back)
        #     card.current_image = card.back
#endregion
class Card():
    def __init__(self, suit, value, deck_olio):
        self.suit = suit
        self.value = value
        self.image = ImageTk.PhotoImage(Image.open("./cards/"+str(suit)+"_"+str(value)+".png").resize((128,128)))
        self.back = ImageTk.PhotoImage(Image.open("./cards/card_back.png").resize((128,128)))
        # self.button = Button(image=self.back, command=lambda:deck_olio.flip_card(self))     
        self.button = Button(image=self.back, command=lambda:deck_olio.choose_card(self))                              
        self.current_image = self.back

#region commented                               
    # def flip_card(self):  
    #     if self.current_image == self.back:
    #         self.button.configure(image=self.image)
    #         self.current_image = self.image
    #     else:
    #         self.button.configure(image=self.back)
    #         self.current_image = self.back
#endregion

deck = Deck()

