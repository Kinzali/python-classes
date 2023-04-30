
# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()

# optional: set window dimensions
#win.geometry("700x350")

images=[None]*5
buttons=[None]*5


# TEHTÄVÄ 1:Muuta allaolevaa koodia niin, että kaikki samat 
# toiminnot tapahtuvat yhden for-loopin sisällä!
#------------------------------------------------------------------------------------------------
# img1=Image.open('spade_1.png')
# img2=Image.open('spade_2.png')
# img3=Image.open('spade_3.png')
# img4=Image.open('spade_4.png')
# img5=Image.open('spade_5.png')

# Resize the image in the given (width, height)
# img1=img1.resize((128,128))
# img2=img2.resize((128,128))
# img3=img3.resize((128,128))
# img4=img4.resize((128,128))
# img5=img5.resize((128,128))

# Convert the image in TkImage
# img1=ImageTk.PhotoImage(img1)
# img2=ImageTk.PhotoImage(img2)
# img3=ImageTk.PhotoImage(img3)
# img4=ImageTk.PhotoImage(img4)
# img5=ImageTk.PhotoImage(img5)

# # Display the image with label
# button1=Button(win, image=img1)
# button2=Button(win, image=img2)
# button3=Button(win, image=img3)
# button4=Button(win, image=img4)
# button5=Button(win, image=img5)

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)
# button5.pack(side=LEFT)
#------------------------------------------------------------------------------------------------

# FOR-LOOPPIIN HELPOTUSTA:
for i ...
    image = Image.open('1_' + ...)+'.png')
    ...resizet tähän..
    images[i] pitää konvertoida photoimageksi..
    buttons[i] = Button..
    ..[i].pack..

win.mainloop()

# Tehtävä 2:
Luo luokka Deck, jossa konstruktorissa:
- initialisoit Tk-ohjelman self.win -muuttujaan
- asetat ylläolevat images=[None]*5 ja buttons=[None]*5 olion käyttöön, eli self.images ja self.buttons..
- kutsut saman luokan create_deck()-metodia, johon siirrät 1.tehtävän for-loopin
- lopuksi konstruktorissa kutsut self.win.mainloop()

Kun teet olion 
deck = Deck() # ohjelma näyttää kortit, jotka olet for-loopin rangeen asettanut (esim. 5 korttia samasta maasta, numerot 1-5)

