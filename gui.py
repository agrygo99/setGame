from tkinter import *
from PIL import ImageTk, Image
import glob
import random
import Deck
Deck = Deck.Deck
root = Tk()
root.title = "Set Game"
#globals
deck = Deck()

ranPic = Label(root)
ranPic.grid(row=0, column=0, columnspan=4)


def populateGrid():
    global image_1
    global image_2
    global image_3
    global image_4
    global image_5
    global image_6
    global image_7
    global image_8
    global image_9
    global image_10
    global image_11
    global image_12
    currentGrid =  []
    for i in range(12):
        currentGrid.append(deck.getCard(i))
    image_1 = ImageTk.PhotoImage(Image.open(currentGrid[0].image))
    image_2 = ImageTk.PhotoImage(Image.open(currentGrid[1].image))
    image_3 = ImageTk.PhotoImage(Image.open(currentGrid[2].image))
    image_4 = ImageTk.PhotoImage(Image.open(currentGrid[3].image))
    image_5 = ImageTk.PhotoImage(Image.open(currentGrid[4].image))
    image_6 = ImageTk.PhotoImage(Image.open(currentGrid[5].image))
    image_7 = ImageTk.PhotoImage(Image.open(currentGrid[6].image))
    image_8 = ImageTk.PhotoImage(Image.open(currentGrid[7].image))
    image_9 = ImageTk.PhotoImage(Image.open(currentGrid[8].image))
    image_10 = ImageTk.PhotoImage(Image.open(currentGrid[9].image))
    image_11 = ImageTk.PhotoImage(Image.open(currentGrid[10].image))
    image_12 = ImageTk.PhotoImage(Image.open(currentGrid[11].image))
    card_1["image"] = image_1
    card_2["image"] = image_2
    card_3["image"] = image_3
    card_4["image"] = image_4
    card_5["image"] = image_5
    card_6["image"] = image_6
    card_7["image"] = image_7
    card_8["image"] = image_8
    card_9["image"] = image_9
    card_10["image"] = image_10
    card_11["image"] = image_11
    card_12["image"] = image_12
    ranPic["image"] = image_1
    print(image_1)
# function defs
def newGame():
    card_1.grid_forget
    global ranPic
    deck.shuffle()
    populateGrid()
'''
    num = random.randint(0, 30)
    ranPic = Label(root, image=imageList[num])
    ranPic.grid(row=0, columnspan=4)
'''

button_5 = Button(root, text="New Game", padx=10, pady=10, command=newGame)
button_5.grid(row=6, column=1, columnspan=3)


def hotSays():
    return

def disableButton():
    pass


card_1 = Button(root, padx=10, pady=10)
card_2 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_3 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_4 = Button(
    root,
    padx=10,
    pady=10
)
card_5 = Button(
    root,
    padx=10,
    pady=10,
    command=newGame
)
card_6 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_7 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_8 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_9 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_10 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_11 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_12 = Button(
    root,
    padx=10,
    pady=10,
    command=hotSays
)
card_1.grid(row=2, column=1)
card_2.grid(row=2, column=2)
card_3.grid(row=2, column=3)
card_4.grid(row=2, column=4)
card_5.grid(row=3, column=1)
card_6.grid(row=3, column=2)
card_7.grid(row=3, column=3)
card_8.grid(row=3, column=4)
card_9.grid(row=4, column=1)
card_10.grid(row=4, column=2)
card_11.grid(row=4, column=3)
card_12.grid(row=4, column=4)


root.mainloop()
