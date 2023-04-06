# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:59:22 2023

@author: rana_
"""


"""
Ask the user to input a string and then print it out onto the screen in reverse order
(use loop)
"""

val = input("Enter a string --> ")

# Solution 1
for i in range(len(val)-1,-1,-1):
    print(val[i], end='')
    

# Solution 2
print()
print("\n",val[::-1])


# Solution 3
val1 = ''
for char in val:
    val1 = char + val1
    
print()
print(val1)