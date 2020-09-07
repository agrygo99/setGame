from tkinter import *
from PIL import ImageTk, Image
import glob
import random
import Deck
import setGame
Deck = Deck.Deck
root = Tk()
root.title = "Set Game"
#globals
currentGrid =  []
selectedCards = []
cardButtons = []
cardIndexList = []
deckIndex = 11
deckIndexList = []

#card selected
card_1_selected = 0
card_2_selected = 0
card_3_selected = 0
card_4_selected = 0
card_5_selected = 0
card_6_selected = 0
card_7_selected = 0
card_8_selected = 0
card_9_selected = 0
card_10_selected = 0
card_11_selected = 0
card_12_selected = 0

def populateImage(cardButtons,cardIndexList,deckIndexList):
    global popImage1
    global popImage2
    global popImage3

    currentGrid[cardIndexList[0]] = deck.getCard(deckIndexList[0])
    currentGrid[cardIndexList[1]] = deck.getCard(deckIndexList[1])
    currentGrid[cardIndexList[2]] = deck.getCard(deckIndexList[2])
    popImage1 = ImageTk.PhotoImage(Image.open(currentGrid[cardIndexList[0]].image))
    popImage2 = ImageTk.PhotoImage(Image.open(currentGrid[cardIndexList[1]].image))
    popImage3 = ImageTk.PhotoImage(Image.open(currentGrid[cardIndexList[2]].image))
    cardButtons[0]['image'] = popImage1
    cardButtons[1]['image'] = popImage2
    cardButtons[2]['image'] = popImage3
    cardButtons[0]["highlightbackground"] = '#FFFFFF'
    cardButtons[1]["highlightbackground"] = '#FFFFFF'
    cardButtons[2]["highlightbackground"] = '#FFFFFF'
    cardButtons.clear()
    cardIndexList.clear()
    deckIndexList.clear()
def selectionManager(selectedCards,cardButtons,cardIndexList):
    global deckIndex
    if len(selectedCards) == 3:
        isSet = setGame.isSet(selectedCards[0], selectedCards[1],selectedCards[2])
        if isSet:
            status["text"] = "Yay! You made a set!"
            for cardIndex in cardIndexList:
                deckIndex += 1
                deckIndexList.append(deckIndex)
                deck.removeCard(cardIndex)
            selectedCards.clear()
            populateImage(cardButtons, cardIndexList,deckIndexList)
        else:
            status["text"] = "Try Again"
            for cardButton in cardButtons:
                cardButton["highlightbackground"] = '#FFFFFF'
                selectedCards.remove(currentGrid[cardIndex])
                cardButtons.remove(cardButton)
                cardIndexList.remove(cardIndex)

def processButton(timeSelected,selectedCards,cardButton,cardIndex):
    if timeSelected == 1:
        cardButton["highlightbackground"] = '#000000'
        selectedCards.append(currentGrid[cardIndex])
        cardButtons.append(cardButton)
        cardIndexList.append(cardIndex)
        selectionManager(selectedCards,cardButtons,cardIndexList)
        return 1
    else:
        cardButton["highlightbackground"] = '#FFFFFF'
        selectedCards.remove(currentGrid[cardIndex])
        cardButtons.remove(cardButton)
        cardIndexList.remove(cardIndex)
        return 0
def card_1_click(selectedCards):
    global card_1_selected
    card_1_selected += 1
    cardIndex = 0
    card_1_selected = processButton(card_1_selected,selectedCards,card_1,cardIndex)

def card_2_click(selectedCards):
    global card_2_selected
    card_2_selected += 1
    cardIndex = 1
    card_2_selected = processButton(card_2_selected,selectedCards,card_2,cardIndex)


def card_3_click(selectedCards):
    global card_3_selected
    card_3_selected += 1
    cardIndex = 2
    card_3_selected = processButton(card_3_selected,selectedCards,card_3,cardIndex)
def card_4_click(selectedCards):
    global card_4_selected
    card_4_selected += 1
    cardIndex = 3
    card_4_selected = processButton(card_4_selected,selectedCards,card_4,cardIndex)
def card_5_click(selectedCards):
    global card_5_selected
    card_5_selected += 1
    cardIndex = 4
    card_5_selected = processButton(card_5_selected,selectedCards,card_5,cardIndex)
def card_6_click(selectedCards):
    global card_6_selected
    card_6_selected += 1
    cardIndex = 5
    card_6_selected = processButton(card_6_selected,selectedCards,card_6,cardIndex)
def card_7_click(selectedCards):
    global card_7_selected
    card_7_selected += 1
    cardIndex = 6
    card_7_selected = processButton(card_7_selected,selectedCards,card_7,cardIndex)
def card_8_click(selectedCards):
    global card_8_selected
    card_8_selected += 1
    cardIndex = 7
    card_8_selected = processButton(card_8_selected,selectedCards,card_8,cardIndex)
def card_9_click(selectedCards):
    global card_9_selected
    card_9_selected += 1
    cardIndex = 8
    card_9_selected = processButton(card_9_selected,selectedCards,card_9,cardIndex)
def card_10_click(selectedCards):
    global card_10_selected
    card_10_selected += 1
    cardIndex = 9
    card_10_selected = processButton(card_10_selected,selectedCards,card_10,cardIndex)
def card_11_click(selectedCards):
    global card_11_selected
    card_11_selected += 1
    cardIndex = 10
    card_11_selected = processButton(card_11_selected,selectedCards,card_11,cardIndex)
def card_12_click(selectedCards):
    global card_12_selected
    card_12_selected += 1
    cardIndex = 11
    card_12_selected = processButton(card_12_selected,selectedCards,card_12,cardIndex)

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
    global currentGrid


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
# function defs
def newGame():
    global deck
    deck = Deck()
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

#Buttons
card_1 = Button(root, padx=10, pady=10, command=lambda: card_1_click(selectedCards))
card_2 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_2_click(selectedCards)
)
card_3 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_3_click(selectedCards)
)
card_4 = Button(
    root,
    padx=10,
    pady=10,
    command =lambda: card_4_click(selectedCards)
)
card_5 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_5_click(selectedCards)
)
card_6 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_6_click(selectedCards)
)
card_7 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_7_click(selectedCards)
)
card_8 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_8_click(selectedCards)
)
card_9 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_9_click(selectedCards)
)
card_10 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_10_click(selectedCards)
)
card_11 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_11_click(selectedCards)
)
card_12 = Button(
    root,
    padx=10,
    pady=10,
    command=lambda: card_12_click(selectedCards)
)

#Labels
status = Label(root)

#Grid
status.grid(row=0, column=0, columnspan=4)
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
