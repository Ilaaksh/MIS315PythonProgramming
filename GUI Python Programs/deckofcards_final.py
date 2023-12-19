import random
from tkinter import *
from PIL import ImageTk, Image

def randomize():
    rand = random.randint(0, 51)
    ifzero = random.randint(0, 51)
    if rand == 0:
        rand = (rand + ifzero + 1)/2
    return int(rand)

def DealCount():
    global dealNum
    dealNum = dealNum + 1
    print("Deal # " + str(dealNum))
    
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
    
    
window = Tk()
window.title("Deck of Cards")
window.geometry('600x400')
window['bg'] = '#6600cc'

dealNum = 0

Button(
    window,
    text="DEAL", 
    padx=10, 
    pady=5,
    bg='#00DDAA',
    command=NewDeal).place(anchor='n',x=50, y=200)

window.mainloop()
#myImage = Image.open("C:\Users\centr\OneDrive\Documents\TEC 388\DeckOfCards\7_of_hearts.png");
#------------ GUI ends -----
# -----  Randomizing data collection method #2 ------
cardSuit = ["Hearts", "Diamonds", "Clubs", "Spades"]
cardValue = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cardDeck = []
for i in cardSuit:
    #print(i)
    for j in cardValue:
        #print(j + " of " + i)
        cardDeck.append(j + " of " + i)

randomDeckArray = []
for pullCard in range(25):
    r = random.randint(0, 3)
    randSuit = cardSuit[r]
    r = random.randint(0, 12)
    randValue = cardValue[r]
    randomDeckArray.append(randValue + " of " + randSuit)
    print (randValue + " of " + randSuit)

#randValue = random.randint(0, 12)
#print(cardValue[randValue])
#print(len(cardDeck))

#print("length of random deck []" + len(randomDeckArray))
#for x in randomDeckArray:
    #print(randomDeckArray[x])



#print(cardSuit[randSuit])
#print(cardDeck[23])


#for x in range(10):
    #rand = random.randint(0, 51)
    #print(rand)
