# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:23:20 2023

@author: rana_
"""

"""
User input a numeric value 1 to 5 in string format, that value should be printed in numberic format.
Example
    User Input = Three
    Output = 3

"""

while True:
    num = input("Enter numberic value in words: ")
    num = num.lower()
    
    if (num == 'one'):
        print(1)
        break
    elif (num == 'two'):
        print(2)
        break
    elif (num == 'three'):
        print(3)
        break
    elif (num == 'four'):
        print(4)
        break
    elif (num == 'five'):
        print(5)
        break
    else:
        print("Invalid Input")