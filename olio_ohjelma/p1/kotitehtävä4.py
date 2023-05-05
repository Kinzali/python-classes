# # Display the image with label
# button1=Button(win, image=img1)
# button2=Button(win, image=img2)
# button3=Button(win, image=img3)
# button4=Button(win, image=img4)
# button5=Button(win, image=img5)

# Luo lista kuvista
kuvat = [img1, img2, img3, img4, img5]

# Luo for-silmukka, joka luo painikkeen jokaiselle kuvalle
for kuva in kuvat:
    painike = Button(win, image=kuva)
    painike.pack()
