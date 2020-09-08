# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:20:37 2020

@author: ashle
"""
import Card

def matchColor(card1,card2,card3):
     #if colors match
    if (card1.getColor() == card2.getColor() and card2.getColor() == card3.getColor()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def difColor(card1,card2,card3):
    #all different colors
    if (card1.getColor() != card2.getColor() and card2.getColor() != card3.getColor() and card1.getColor() != card3.getColor()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def matchFill(card1,card2,card3):
    #if fills match
    if (card1.getFill() == card2.getFill() and card2.getFill() == card3.getFill()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def difFill(card1,card2,card3):
    #all different fills
    if (card1.getFill() != card2.getFill() and card2.getFill() != card3.getFill() and card1.getFill() != card3.getFill()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def matchShape(card1,card2,card3):
    #if shapes match
    if (card1.getShape() == card2.getShape() and card2.getShape() == card3.getShape()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def difShape(card1,card2,card3):
    #all different shapes
    if (card1.getShape() != card2.getShape() and card2.getShape() != card3.getShape() and card1.getShape() != card3.getShape()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def matchNum(card1,card2,card3):
    #if numbers match
    if (card1.getNumber() == card2.getNumber() and card2.getNumber() == card3.getNumber()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
def difNum(card1,card2,card3):
    #all different numbers
    if (card1.getNumber() != card2.getNumber() and card2.getNumber() != card3.getNumber() and card1.getNumber() != card3.getNumber()):
        #messagebox.showinfo("Congrats!", "Good set!")
        return True
    else:
        return False
    
#takes an input of 3 cards and compares all of their qualities to determine if they form a set or not
#i added pop up windows to say if it is a good set, or an error for nonvalid set
def isSet(card1, card2, card3):
    #3 MATCHES, 1 DISJOINT
    #color,fill,shape same; number different
    if ((matchColor(card1,card2,card3)==True) and (matchFill(card1,card2,card3)==True) and (matchShape(card1,card2,card3)==True) and (difNum(card1,card2,card3)==True)):
        return True
    #color,shape,number same; fill different
    elif (matchColor(card1,card2,card3)==True and matchShape(card1,card2,card3)==True and matchNum(card1,card2,card3)==True and difFill(card1,card2,card3)==True):
        return True
    #color,fill,number same; shape different
    elif (matchColor(card1,card2,card3)==True and matchFill(card1,card2,card3)==True and matchNum(card1,card2,card3)==True and difShape(card1,card2,card3)==True):
        return True
    #shape,fill,number same; color different
    elif (matchNum(card1,card2,card3)==True and matchFill(card1,card2,card3)==True and matchShape(card1,card2,card3)==True and difColor(card1,card2,card3)==True):
        return True
    
    #1 MATCH, 3 DISJOINT
    #color same; shape,fill,number different
    elif (matchColor(card1,card2,card3)==True and difShape(card1,card2,card3)==True and difFill(card1,card2,card3)==True and difNum(card1,card2,card3)==True):
        return True
    #shape same; color,fill,number different
    elif (matchShape(card1,card2,card3)==True and difColor(card1,card2,card3)==True and difFill(card1,card2,card3)==True and difNum(card1,card2,card3)==True):
        return True
    #fill same; color,shape,number different
    elif (matchFill(card1,card2,card3)==True and difShape(card1,card2,card3)==True and difColor(card1,card2,card3)==True and difNum(card1,card2,card3)==True):
        return True
    #number same; color,shape,fill different
    elif (matchNum(card1,card2,card3)==True and difShape(card1,card2,card3)==True and difFill(card1,card2,card3)==True and difColor(card1,card2,card3)==True):
        return True
    
    #ALL DISJOINT
    elif (difColor(card1,card2,card3)==True and difFill(card1,card2,card3) and difShape(card1,card2,card3)==True and difNum(card1,card2,card3)==True):
        return True
    elif card1 is None or card2 is None or card3 is None:
        return False
    #not a set
    else:
        #makes an error pop up, not a set
        #messagebox.showerror("Error", "Not a valid set")
        return False
        
#lines 53 through 72 from Prof Szecsei Card.py file
