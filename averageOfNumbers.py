# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:00:59 2023

@author: rana_
"""

"""
Take multiple input from user and print its average.
"""


nums = []
flag =  1

while (flag != 0):
    n = input("Enter Number: --> ")
    
    if (n.isdigit()):        
        nums.append(int(n))
        print("Press 1 for next number")
        print("Press 0 to get the average")
        y = input("--> ")
        if (y.isdigit()):
            y = int(y)
            if y == 1:
                flag = 1
            elif y == 0 :
                flag = 0
            else:
                print("Invalid Input")
        else:
            print("It is not a  number")
            
    else:
        print("Its not a number")
        
# Find Average
sum = 0

for number in nums:
    sum += number

avg = sum/len(nums)

print("Average of entered numbers are: ", avg)