#luo luokka Deck, ja tee sille konstruktori, joka ei syötä imia parametreja oliota luodessa.
# luo konstruktorissa:
#     -Tk-luokasta olio(self.win=TK())
#     -self.images
#     -self.buttons
#     -kutsu self.create_deck()
#     -luopuksi self.win.mainloop()

# luo metodi create_deck, siirrä edellisen tehdävän for-looppi siihen, 
# tee tarvittavat self-muutokset

# luo lopuksi olio Deck-luokasta, loputulos tulisi olla sama kuin edellisessä tehtävässä
import os

from tkinter import*
from PIL import Image, ImageTk
import random

print(os.getcwd())


class Deck:
    def __init__(self):
        self.win = Tk()
        self.images= []
        self.buttons=[]
        self.win.bind('<Return>', lambda event:self.click2())
        self.create_deck()
        self.win.mainloop()
        
    def create_deck(self):
        for i in range(13):
            image = Image.open(os.getcwd()+'/cards/1_'+str(i+1)+'.png')
            image= image.resize((128,128))
            self.images.append(image)
            self.images[i] = ImageTk.PhotoImage(self.images[i])
            button= Button(self.win, image=self.images[i],command=lambda num=i:self.click(num))
            self.buttons.append(Button)
            self.buttons[-1].grid(row=0, column=i)   

    def click(self,num):
        #kun korttia painaa, muuttuu sen kuva 1_1.png:ksi
        self.buttons[num].configure(image=self.images[0])

    def click2(self):
        print("click2")
        
deck = Deck()