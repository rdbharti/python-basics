# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:20:30 2023

@author: rana_
"""


"""
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

"""

suits = ['diabond','heart','spade','club']
cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck = dict()
for suit in suits:
    deck[suit] = cards
        
print(deck)