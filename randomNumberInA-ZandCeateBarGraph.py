# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:27:33 2023

@author: rana_
"""

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
import random
import matplotlib.pyplot as plt

alpabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

x = []

for i in range(0,26):
    x.append(random.randint(1, 1000))
    
d = dict(zip(alpabets,x))



plt.bar(list(d.keys()),list(d.values()))