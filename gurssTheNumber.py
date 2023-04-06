# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:31:43 2023

@author: rana_
"""

"""
Ask user to guess a number between 1 and 10 (inclusive), if the user number is greater than the number then print 'too high', if the number is less than the number
then print number is too low. Untill user guess the correct number

"""

import random
num = random.randint(1, 10)
while True:    
    user_num = int(input("Enter a number between 1 and 10 "))
    num_check = 0
    for i in range(1,11):
        if (i == user_num):
            num_check = 1
    if (num_check == 1):
       if (user_num > num):
           print("User number is too HIGH")
       if (user_num < num):
           print("User Number is too LOW")
       elif (user_num == num):
           print("Bingo! Correct Number is ", num)
           break
    if (num_check == 0):
        print("Invalid Input!!")
           

