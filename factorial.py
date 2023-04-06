# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:32:23 2023

@author: rana_
"""

num = input("Enter a number: --> ")
if (num.isdigit()):
    num = int(num)
    fact = 1
    for n in range(1,num+1):
        fact *= n
    print(f"Factorial of {num} is {fact}")
else:
    print("Invalid Input")