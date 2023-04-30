from tkinter import *
from PIL import Image, ImageTk
import os

class Deck():
    def __init__(self):
        self.win=Tk()
        self.cards = []
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
                pass # lisää Card-olio self.cards:iin, 
        
        # ja tee tarvittavat value/suit -muutokset
            
    def deal(self):
        # 2 sisäkkäistä loopia, jotta kortit saadaan näkymään gridissä
        index = 0
        for row in range(1,5): # 1-4
            for column in range(1,14):
                self.cards[index].button.grid(row=row, column=column-1)
                index += 1
        
  
    def choose_card(self,card):
        if self.chosen1 == None:
            self.chosen1 == card
            card.button.configure(image=card.image)
        elif self.chosen2== None:
            self.chosen2= card
            card.button.configure(image=card.image)
            self.check_cards()

    def check_cards(self):
        if self.chosen1.value == self.chosen2.value:
            self.chosen1.button["state"]= DISABLED
            self.chosen2.button["state"]= DISABLED
            
            self.chosen1 = None
            self.chosen2 = None
            
        else:
            self.win.after(1000,self.reset_cards)
            
    def reset_cards(self):
        self.chosen1.buttons.configure(image=self.chosen1.back)
        self.chosen2.buttons.configure(image=self.chosen2.back)
        self.chosen1 = None
        self.chosen2 = None
        
    
class Card():
    def __init__(self, suit, value, deck_olio):
        self.suit = suit
        self.value = value
        self.image = ImageTk.PhotoImage(Image.open(os.getcwd()/"cards/"+str(suit)+"_"+str(value)+".png").resize((128,128)))
        #self.button = Button(image=self.image)    
        self.back = ImageTk.PhotoImage(Image.open(os.getcwd()+"/cards/cards_back.png").resize((128,128)))
        self.Button = Button(image=self.back,  command=lambda:deck_olio.choose_card(self))
        self.current_image = self.back

deck = Deck()


# HARJOITUS: KOITA SAADA KORTIT NÄKYVIIN NIIN, ETTÄ 1.RIVILLÄ ON HERTAT 1-13,
# 2. RIVILLÄ RUUDUT 13 JNE. ELI 4 RIVIIN.