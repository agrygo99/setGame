from tkinter import *
from PIL import ImageTk, Image
from itertools import *
import glob
import random
import sys
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
timeSelectedList = []

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

def setOnGrid():
    cardCombinations = list(combinations(currentGrid, 3))
    # print(cardCombinations)
    for combination in cardCombinations:
        flag = setGame.isSet(combination[0], combination[1], combination[2])
        if flag:
            return True
    return False

def draw():
    status["text"] = "Redrawing"
    cardBut = [card_1,card_2,card_3]
    cardIdxList = [0,1,2]
    deckIndexList = [deckIndex+1, deckIndex+2, deckIndex+3]
    populateImage(cardBut, cardIdxList, deckIndexList)
    

def resetTimeSelected():
    global card_1_selected
    global card_2_selected
    global card_3_selected
    global card_4_selected
    global card_5_selected
    global card_6_selected
    global card_7_selected
    global card_8_selected
    global card_9_selected
    global card_10_selected
    global card_11_selected
    global card_12_selected

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
    global keepImage1
    global keepImage2
    global keepImage3
    global keepImage4
    global keepImage5
    global keepImage6
    global keepImage7
    global keepImage8
    global keepImage9

    drewThree = False

    if all(card is None for card in deck.cardList) and setOnGrid() == False:
        status["text"] = "Game Over!"
        disableButtons()
        return
    if all(card is None for card in deck.cardList):
        currentGrid[cardIndexList[0]] = None
        currentGrid[cardIndexList[1]] = None
        currentGrid[cardIndexList[2]] = None
        cardButtons[0]['image'] = None
        cardButtons[1]['image'] = None
        cardButtons[2]['image'] = None
        cardButtons[0]['state'] = DISABLED
        cardButtons[1]['state'] = DISABLED
        cardButtons[2]['state'] = DISABLED
        cardButtons.clear()
        cardIndexList.clear()
        deckIndexList.clear()
        resetTimeSelected()
        return
    allCardButtons = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_11,card_12]
    allCardIndex = [0,1,2,3,4,5,6,7,8,9,10,11]
    for cardButton in cardButtons:
        allCardButtons.remove(cardButton)
    for cardIndex in cardIndexList:
        allCardIndex.remove(cardIndex)

    currentGrid[cardIndexList[0]] = deck.getCard(deckIndexList[0])
    currentGrid[cardIndexList[1]] = deck.getCard(deckIndexList[1])
    currentGrid[cardIndexList[2]] = deck.getCard(deckIndexList[2])
    tries = 0
    while setOnGrid() is False:
        tries += 1
        draw()
        deck.removeCard(deckIndexList[0])
        deck.removeCard(deckIndexList[1])
        deck.removeCard(deckIndexList[2])
        deck.insertBackOfDeck(deckIndexList[0])
        deck.insertBackOfDeck(deckIndexList[1])
        deck.insertBackOfDeck(deckIndexList[2])
        drewThree = True
        if tries > 81:
            status["text"] = "Game Over!"
            disableButtons()

    #print(str(cardIndexList))
    #print(str(deckIndexList))
    if not drewThree:
        deck.removeCard(deckIndexList[0])
        deck.removeCard(deckIndexList[1])
        deck.removeCard(deckIndexList[2])
    popImage1 = ImageTk.PhotoImage(Image.open(currentGrid[cardIndexList[0]].image))
    popImage2 = ImageTk.PhotoImage(Image.open(currentGrid[cardIndexList[1]].image))
    popImage3 = ImageTk.PhotoImage(Image.open(currentGrid[cardIndexList[2]].image))
    keepImage1 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[0]].image))
    keepImage2 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[1]].image))
    keepImage3 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[2]].image))
    keepImage4 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[3]].image))
    keepImage5 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[4]].image))
    keepImage6 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[5]].image))
    keepImage7 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[6]].image))
    keepImage8 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[7]].image))
    keepImage9 = ImageTk.PhotoImage(Image.open(currentGrid[allCardIndex[8]].image))
    #print(currentGrid[cardIndexList[0]].image)
    #print(currentGrid[cardIndexList[1]].image)
    #print(currentGrid[cardIndexList[2]].image)
    cardButtons[0]['image'] = popImage1
    cardButtons[1]['image'] = popImage2
    cardButtons[2]['image'] = popImage3
    allCardButtons[0]['image'] = keepImage1
    allCardButtons[1]['image'] = keepImage2
    allCardButtons[2]['image'] = keepImage3
    allCardButtons[3]['image'] = keepImage4
    allCardButtons[4]['image'] = keepImage5
    allCardButtons[5]['image'] = keepImage6
    allCardButtons[6]['image'] = keepImage7
    allCardButtons[7]['image'] = keepImage8
    allCardButtons[8]['image'] = keepImage9
    cardButtons[0]["highlightbackground"] = '#FFFFFF'
    cardButtons[0]["bg"] = '#FFFFFF'
    cardButtons[1]["highlightbackground"] = '#FFFFFF'
    cardButtons[1]["bg"] = '#FFFFFF'
    cardButtons[2]["highlightbackground"] = '#FFFFFF'
    cardButtons[2]["bg"] = '#FFFFFF'
    cardButtons.clear()
    cardIndexList.clear()
    deckIndexList.clear()
    resetTimeSelected()
def selectionManager(selectedCards,cardButtons,cardIndexList):
    global deckIndex
    if len(selectedCards) == 3:
        isSet = setGame.isSet(selectedCards[0], selectedCards[1],selectedCards[2])
        if isSet:
            status["text"] = "Yay! You made a set!"
            for cardIndex in cardIndexList:
                deckIndex += 1
                deckIndexList.append(deckIndex)
            selectedCards.clear()
            populateImage(cardButtons, cardIndexList,deckIndexList)
        else:
            status["text"] = "Try Again"
            for cardButton in cardButtons:
                cardButton["highlightbackground"] = '#FFFFFF'
                cardButton["bg"] = '#FFFFFF'
            selectedCards.clear()
            cardButtons.clear()
            cardIndexList.clear()
            resetTimeSelected()

def processButton(timeSelected,selectedCards,cardButton,cardIndex):
    if timeSelected == 1:
        cardButton["highlightbackground"] = '#000000'
        cardButton["bg"] = '#000000'
        selectedCards.append(currentGrid[cardIndex])
        cardButtons.append(cardButton)
        cardIndexList.append(cardIndex)
        selectionManager(selectedCards,cardButtons,cardIndexList)
        if len(selectedCards) == 0:
            return 0
    else:
        cardButton["highlightbackground"] = '#FFFFFF'
        cardButton["bg"] = '#FFFFFF'
        selectedCards.remove(currentGrid[cardIndex])
        cardButtons.remove(cardButton)
        cardIndexList.remove(cardIndex)
        return 0
def card_1_click():
    global card_1_selected
    card_1_selected += 1
    cardIndex = 0
    card_1_selected = 1 if processButton(card_1_selected,selectedCards,card_1,cardIndex) is None else 0

def card_2_click():
    global card_2_selected
    card_2_selected += 1
    cardIndex = 1
    card_2_selected = 1 if processButton(card_2_selected,selectedCards,card_2,cardIndex) is None else 0


def card_3_click():
    global card_3_selected
    card_3_selected += 1
    cardIndex = 2
    card_3_selected = 1 if processButton(card_3_selected,selectedCards,card_3,cardIndex) is None else 0
def card_4_click():
    global card_4_selected
    card_4_selected += 1
    cardIndex = 3
    card_4_selected = 1 if processButton(card_4_selected,selectedCards,card_4,cardIndex) is None else 0
def card_5_click():
    global card_5_selected
    card_5_selected += 1
    cardIndex = 4
    card_5_selected = 1 if processButton(card_5_selected,selectedCards,card_5,cardIndex) is None else 0
def card_6_click():
    global card_6_selected
    card_6_selected += 1
    cardIndex = 5
    card_6_selected = 1 if processButton(card_6_selected,selectedCards,card_6,cardIndex) is None else 0
def card_7_click():
    global card_7_selected
    card_7_selected += 1
    cardIndex = 6
    card_7_selected = 1 if processButton(card_7_selected,selectedCards,card_7,cardIndex) is None else 0
def card_8_click():
    global card_8_selected
    card_8_selected += 1
    cardIndex = 7
    card_8_selected = 1 if processButton(card_8_selected,selectedCards,card_8,cardIndex) is None else 0
def card_9_click():
    global card_9_selected
    card_9_selected += 1
    cardIndex = 8
    card_9_selected = 1 if processButton(card_9_selected,selectedCards,card_9,cardIndex) is None else 0
def card_10_click():
    global card_10_selected
    card_10_selected += 1
    cardIndex = 9
    card_10_selected = 1 if processButton(card_10_selected,selectedCards,card_10,cardIndex) is None else 0
def card_11_click():
    global card_11_selected
    card_11_selected += 1
    cardIndex = 10
    card_11_selected = 1 if processButton(card_11_selected,selectedCards,card_11,cardIndex) is None else 0
def card_12_click():
    global card_12_selected
    card_12_selected += 1
    cardIndex = 11
    card_12_selected = 1 if processButton(card_12_selected,selectedCards,card_12,cardIndex) is None else 0

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

    for i in range(12):
        currentGrid.append(deck.getCard(i))
        deck.removeCard(i)
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
    #print(len(deck.cardList))
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

def quitGame():
    sys.exit()

button_6 = Button(root, text="Quit Game", padx=10, pady=10, command=quitGame)
button_6.grid(row=6, column=2, columnspan=3)

def checkNumSets():
    status["text"]= int(setGame.getCount() / 2)

button_7 = Button(root, text="Check # of Sets", padx=10,pady=10, command=checkNumSets)
button_7.grid(row=6, column=3, columnspan=3)

def hotSays():
    return

def disableButtons():
    allCardButtons = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_11,card_12]
    for button in allCardButtons:
        button["status"] = DISABLED

#Buttons
card_1 = Button(root, padx=10, pady=10, command=card_1_click)
card_2 = Button(
    root,
    padx=10,
    pady=10,
    command=card_2_click
)
card_3 = Button(
    root,
    padx=10,
    pady=10,
    command=card_3_click
)
card_4 = Button(
    root,
    padx=10,
    pady=10,
    command =card_4_click
)
card_5 = Button(
    root,
    padx=10,
    pady=10,
    command=card_5_click
)
card_6 = Button(
    root,
    padx=10,
    pady=10,
    command=card_6_click
)
card_7 = Button(
    root,
    padx=10,
    pady=10,
    command=card_7_click
)
card_8 = Button(
    root,
    padx=10,
    pady=10,
    command=card_8_click
)
card_9 = Button(
    root,
    padx=10,
    pady=10,
    command=card_9_click
)
card_10 = Button(
    root,
    padx=10,
    pady=10,
    command=card_10_click
)
card_11 = Button(
    root,
    padx=10,
    pady=10,
    command=card_11_click
)
card_12 = Button(
    root,
    padx=10,
    pady=10,
    command=card_12_click
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
