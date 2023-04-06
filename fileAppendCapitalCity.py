# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:56:56 2023

@author: rana_
"""

'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''

def capitals(cap):
    with open("capitals.txt","a") as my_file:
        my_file.write(", " + cap)
        
capitalCity = input("Enter a Capital City -> ")

capitals(capitalCity)