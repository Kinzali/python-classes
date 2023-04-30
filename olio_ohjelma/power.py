from tkinter import*

win = Tk()

win.geometry("640x480")

win.title("POWER!!!")

def power():
    numero = int(entry.get())
    numero *= numero
    label = Label(win, text=str(numero))
    label.pack()

#luodaan input tekstikenttä, johon voi kirjoittaa:

entry = Entry(win,width=40)

#näytetään entry-widget win-objektiin:

entry.pack(ipadx=20, pady=20)

#luodaan buttoni, joka ajaa power()-funktion:
button = Button(win, text="LASKE",command=power)
button.pack()

win.mainloop()