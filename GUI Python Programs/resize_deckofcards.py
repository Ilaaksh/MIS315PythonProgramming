import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def randomize():
    rand = random.randint(0, 51)
    ifzero = random.randint(0, 51)
    if rand == 0:
        rand = (rand + ifzero + 1)/2
    return int(rand)

def NewCard():
    cardImage = ImageTk.PhotoImage(Image.open('./CardDeckSmall/'+str(randomize())+'.png'))
    return cardImage

def NewDeal():
    global cardImage1, cardImage2, cardImage3, cardImage4, cardImage5
    DealCount()
    cardImage1 = NewCard()
    cardImage2 = NewCard()
    cardImage3 = NewCard()
    cardImage4 = NewCard()
    cardImage5 = NewCard()

    label1 = Label(window, image=cardImage1).place(anchor='n', x=50, y=10)
    label2 = Label(window, image=cardImage2).place(anchor='n',x=125, y=10)
    label3 = Label(window, image=cardImage3).place(anchor='n',x=200, y=10)
    label4 = Label(window, image=cardImage4).place(anchor='n',x=275, y=10)
    label5 = Label(window, image=cardImage5).place(anchor='n',x=350, y=10)

window = Tk() #constructor
window.title("Black Jack game")
window.geometry('850x600')
window.configure(background = "green")

#frm = ttk.Frame(window, padding=50)
#frm.grid(column=2, row=2)
Label(window, text="BLACK JACK").place(relx=0.5, anchor=N)

Label(window, text="Dealer").place(relx=0.1, rely=0.2, anchor=NW)

Label(window, text="Player").place(relx=0.1, rely=0.4, anchor=SW)

Button(
    window,
    text="DEAL").place(relheight=0.1, relwidth=0.3, relx=0.5, rely=0.9, anchor=S)
window.mainloop()