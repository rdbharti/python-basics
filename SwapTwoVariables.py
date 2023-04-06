# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:25:12 2023

@author: rana_
"""

num1=0
num2=0

while True:
    check = 0
    x = input("Enter first Nubmer: ")
    if (x.isdigit()):
        x = int(x)
        check = check+1
    
    y = input("Enter Second Nubmer: ")
    if (y.isdigit()):
        y = int(y)
        check = check+1
    
    if (check == 2):
        num1 = x
        num2 = y
        break
    else:
        print("Invalid input")
        
# print("Original\nNum1 = ",num1, "num2 = ",num2)
# num1 = num1+num2
# num2 = num1-num2
# num1 = num1-num2
        
# print("Swapped \nnum1 = ",num1, "num2 = ",num2)

print("Original\nNum1 = ",num1, "num2 = ",num2)
num1, num2 = num2, num1        
print("Swapped \nnum1 = ",num1, "num2 = ",num2)