import random
from tkinter import *
from PIL import ImageTk, Image

def createDeckofCards():
    """Function to create a deck of 52 cards represented as integers."""
    deck = [i for i in range(1, 53)]
    random.shuffle(deck)
    return deck

def dealCards(deck, hand, images, count=1):
    """Deals a specific number of cards from the deck to a hand."""
    for _ in range(count):
        if deck:
            card = deck.pop()
            hand.append(card)
            cardImage = ImageTk.PhotoImage(Image.open(f'/Users/ilaakshmishra/Documents/MIS315-Python Programming/GUI Python Programs/CardDeckSmall/{card}.png'))
            images.append(cardImage)
        else:
            print("No more cards in the deck.")

def newDeal(window, playerImages, dealerImages):
    """Displays the initial deal on the GUI."""
    for i, img in enumerate(dealerImages):
        Label(window, image=img).place(anchor='n', x=100 + 75*i, y=150)

    for i, img in enumerate(playerImages):
        Label(window, image=img).place(anchor='n', x=100 + 75*i, y=340)

def playerDeal():
    """Handles the player's request for an additional card."""
    global cardCounter
    if deck:
        dealCards(deck, playerHand, playerImages, 1)
        Label(window, image=playerImages[-1]).place(anchor='n', x=100 + 75*cardCounter, y=340)
        cardCounter += 1
    else:
        print("No more cards in the deck.")

# Initialize the game
window = Tk()
window.title("Black Jack Game")
window.geometry('850x600')
window.configure(background="green")

deck = createDeckofCards()
playerHand, dealerHand = [], []
playerImages, dealerImages = [], []
cardCounter = 2

# Deal initial cards
dealCards(deck, dealerHand, dealerImages, 2)
dealCards(deck, playerHand, playerImages, 2)
newDeal(window, playerImages, dealerImages)

# GUI Components
Label(window, text="BLACK JACK").place(relx=0.5, anchor=N)
Label(window, text="Dealer:").place(relx=0.1, rely=0.2, anchor=NW)
Label(window, text="Player:").place(relx=0.1, rely=0.55, anchor=SW)
Button(window, text="DEAL", command=playerDeal).place(relheight=0.1, relwidth=0.3, relx=0.5, rely=0.9, anchor=S)

window.mainloop()
