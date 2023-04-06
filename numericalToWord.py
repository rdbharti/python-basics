# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:50:41 2023

@author: rana_
"""

"""
Write a code to ask the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value.
So for example
if user inputs '2' the output should be Two
Reject the input if the input number is not in range 1 to 5.

"""

while True:
    number = int(input("Enter a number between 1 and 5 inclusive \n--> "))
    if (number == 1):
        print("One")
        break
    elif (number == 2):
        print("Two")
        break
    elif (number == 3):
        print("Three")
        break
    elif (number == 4):
        print("Four")
        break
    elif (number == 5):
        print("Five")
        break
    else:
        print("Number 1 - 5 acceptable")
