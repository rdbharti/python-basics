# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:06:23 2023

@author: rana_
"""

num1 = input("enter a number 1-20 --> ")
num2 = input("enter another number 1-20 --> ")

if (num1.isdigit() and num2.isdigit()):
    num1 = int(num1)
    num2 = int(num2)
    
    if (num1 > 0 and num1 <= 20):
        if (num2 > 0 and num2 <= 20):
            # Main Code
            if (num1 > 15 and num2 > 15):
                print("Product",num1*num2)
            elif (num1 > 15):
                if (num2 < 15):
                    print("Sum",num1+num2)
            elif (num2 > 15):
                if(num1 < 15):
                    print("Sum",num1+num2)
            else:
                print(0)
        else:
            print("Out of Bound")
    else:
        print("Numbers OUT of BOUND")
    
    
else:
    print("Number enetered is not a digit")