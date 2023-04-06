# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:21:49 2023

@author: rana_
"""

"""
Ask the user for two numbers between 1 and 100. Then count from 
the lower number to the higher number.
Print the results 
"""

n1 = ''
n2 = ''
while True:
    print("Number range 1 - 100")
    n1 = input("Enter Number1: ")
    n2 = input("Enter Number2: ")
    
    
    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        if n1 > 0 and n2 > 0:
            if n1 <= 100 and n2 <= 100:
                if n1 != n2:
                    break
                else:
                    print("Numbers CAN'T be same")
            
            else:
                print("Numbers should NOt be more than 100")
        else:
            print("Numbers should be more than 0")
            
    else:
        print("Invalid Input")

if n1 > n2:
    print(list(range(n2,n1+1)))
else:
    print(list(range(n1,n2+1)))

