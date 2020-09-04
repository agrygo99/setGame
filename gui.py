from tkinter import *
from PIL import ImageTk, Image
import glob
import random

root = Tk()
root.title = "Set Game"

fileList = []
imageList = []
for filename in glob.glob("CardImages/*.gif"):  # assuming gif
    fileList.append(filename)
    im = ImageTk.PhotoImage(Image.open(filename))
    imageList.append(im)
print(fileList[0])
ranPic = Label(root)
ranPic.grid(row=0, column=0, columnspan=4)

ig = ImageTk.PhotoImage(Image.open(fileList[0]))


def newGame():
    global ranPic
    num = random.randint(0, 30)
    ranPic = Label(root, image=imageList[num])
    ranPic.grid(row=0, columnspan=4)


button_5 = Button(root, text="New Game", padx=50, pady=50, command=newGame)
button_5.grid(row=6, column=1, columnspan=3)


def hotSays():
    return


card_1 = Button(root, text="Dog", width=190, height=140, image=ig)
card_2 = Button(
    root,
    text="Snoop",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[1])),
)
card_3 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[2])),
)
card_4 = Button(
    root,
    text="DogBounty",
    width=190,
    height=140,
    image=ImageTk.PhotoImage(Image.open(fileList[3])),
)
card_5 = Button(
    root,
    text="New Game",
    width=190,
    height=140,
    command=newGame,
    image=ImageTk.PhotoImage(Image.open(fileList[4])),
)
card_6 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
)
card_7 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
)
card_8 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
)
card_9 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
)
card_10 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
)
card_11 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
)
card_12 = Button(
    root,
    text="HotDog",
    width=190,
    height=140,
    command=hotSays,
    image=ImageTk.PhotoImage(Image.open(fileList[0])),
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
