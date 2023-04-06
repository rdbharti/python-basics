# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:46:29 2023

@author: rana_
"""

'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''

def power(num1, exp=2):
    return num1**exp

print(power(3,3))