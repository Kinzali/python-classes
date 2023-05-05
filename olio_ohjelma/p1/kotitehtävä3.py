Convert the image in TkImage
# img1=ImageTk.PhotoImage(img1)
# img2=ImageTk.PhotoImage(img2)
# img3=ImageTk.PhotoImage(img3)
# img4=ImageTk.PhotoImage(img4)
# img5=ImageTk.PhotoImage(img5)

from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()

# kuvatiedostojen polut
img_paths = ['kuva1.png', 'kuva2.png', 'kuva3.png', 'kuva4.png', 'kuva5.png']

# käsittele jokainen kuva
tk_images = []
for path in img_paths:
    img = Image.open(path)
    tk_img = ImageTk.PhotoImage(img)
    tk_images.append(tk_img)

# käytä tk_images -listaa tarpeidesi mukaan
label = tk.Label(root, image=tk_images[0])
label.pack()

root.mainloop()
