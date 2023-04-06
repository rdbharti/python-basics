# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:12:54 2023

@author: rana_
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }

cap = input("Enter a Country Name.\n--> ")
cap = cap.capitalize()
if (cap in capitals):
    print(f"{cap} is present in the dictionary.")
else:
    print(f"{cap} is NOT present in the dictionary")