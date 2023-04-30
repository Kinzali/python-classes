from tkinter import *
import os

#python -m venve pelikortit_env
#pelikortit_env/scripts/activate
#pip install pillow
from PIL import Image, ImageTk

# region Tkinter app
win=Tk()

# Image=[None]*5
# buttons= [None]*5

# # asetetaan tiedosto muuttujaan
# Image1 = Image.open('./cards/1_1.png')
# Image2 = Image.open('./cards/1_4.png')

# #muutetaan image-muuttuja näytettävään muotoon:
# Image1= Image.resize((128,128))
# Image2= Image.resize((128,128))
# #muuttutaan image-muuttuja näytettävään muotoon:
# image1 = ImageTk.PhotoImage(Image1)
# image2 = ImageTk.PhotoImage(Image2)

# #tehdään kuvasta nappi, ja asetetaan se applikaatioon:
# button1= Button(win,image=Image1)
# button2= Button(win,image=image2)
print(os.getcwd())
# #sijoitetaan kuva applikaatioon:
# button1.pack(side=LEFT) #parametrein voidaan kertoa, minne kuva sijoitetaan:
# button2.pack(side=LEFT)
images=[]
buttons=[]
for i in range(13):
    image = Image.open(os.getcwd()+'/cards/1_'+str(i+1)+'.png')
    images.append(image.resize((128,128)))
    images[i] = ImageTk.PhotoImage(images[i])
    buttons.append(Button(win, image=images[i]))
    buttons[i].pack(side=LEFT)
    
    
win.mainloop()
#endregion
