# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:20:37 2020

@author: ashle
"""
#import tkinter
#from tkinter import messagebox
#import Card

#root= tkinter.Tk()
#root.withdraw()

#takes an input of 3 cards and compares all of their qualities to determine if they form a set or not
#i added pop up windows to say if it is a good set, or an error for nonvalid set
def isSet(card1, card2, card3):
    if card1 is None or card2 is None or card3 is None:
        return False  
     #if colors match
    if (card1.getColor() == card2.getColor() and card2.getColor() == card3.getColor()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #all different colors
    elif (card1.getColor() != card2.getColor() and card2.getColor() != card3.getColor() and card1.getColor() != card3.getColor()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #if fills match
    elif (card1.getFill() == card2.getFill() and card2.getFill() == card3.getFill()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #all different fills
    elif (card1.getFill() != card2.getFill() and card2.getFill() != card3.getFill() and card1.getFill() != card3.getFill()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #if shapes match
    elif (card1.getShape() == card2.getShape() and card2.getShape() == card3.getShape()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #all different shapes
    elif (card1.getShape() != card2.getShape() and card2.getShape() != card3.getShape() and card1.getShape() != card3.getShape()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #if numbers match
    elif (card1.getNumber() == card2.getNumber() and card2.getNumber() == card3.getNumber()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    #all different numbers
    elif (card1.getNumber() != card2.getNumber() and card2.getNumber() != card3.getNumber() and card1.getNumber() != card3.getNumber()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        #makes an error pop up, not a set
        #messagebox.showerror("Error", "Not a valid set")
        return False