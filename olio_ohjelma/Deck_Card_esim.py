
from tkinter import *
from PIL import Image, ImageTk
import os #built-in moduuli, jossa hyödyllisiä metodeita: https://www.tutorialspoint.com/python/os_file_methods.htm

class Deck():
    def __init__(self):
        self.win=Tk()        
        self.cards = []

        self.fill_deck()
        self.deal()

        self.win.mainloop()

    def fill_deck(self):
        for i in range(1, 6):
            self.cards.append(Card("spade", i)) # getcwd='get current working directory', toimii joka käyttöjärjestelmällä

    def deal(self):
        for i in range(5):
            self.cards[i].cardButton.grid(row=0, column=i)

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = ImageTk.PhotoImage(Image.open(os.getcwd()+"\cards\\"+str(suit)+"_"+str(value)+".png").resize((128,128))) # huom \\ https://www.w3schools.com/python/gloss_python_escape_characters.asp
                          # vie hiiri Button-sanan päälle, niin näet, mitä asetuksia voit asettaa oliota luodessa
        self.cardButton = Button(image=self.image,  command=self.change_card) #huom! ei ()-sulkuja metodin nimen jälkeen
                                                                             

    def change_card(self):        
        self.changed_image = ImageTk.PhotoImage(Image.open('./cards/spade_1.png').resize((128,128))) # pisteellä voi myös viitata nykyiseen hakemistoon
        self.cardButton.configure(image=self.changed_image) # configurella voi muuttaa samoja asetuksia, jotka Button-luokan oliota tehdessä voi asettaa

deck = Deck()

