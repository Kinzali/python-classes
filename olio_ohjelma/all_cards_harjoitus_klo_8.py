from tkinter import *
from PIL import Image, ImageTk

class Deck():
    def __init__(self):
        self.win=Tk()
        self.images=[]
        self.buttons=[]
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
        # 2 for-loopia, jossa kortit näytetään gridissä
        pass

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = ImageTk.PhotoImage(Image.open("./cards/"+str(suit)+"_"+str(value)+".png").resize((128,128)))
        self.button = Button(image=self.image)    

deck = Deck()


# HARJOITUS: KOITA SAADA KORTIT NÄKYVIIN NIIN, ETTÄ 1.RIVILLÄ ON HERTAT 1-13,
# 2. RIVILLÄ RUUDUT 13 JNE. ELI 4 RIVIIN.