# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:29:14 2023

@author: rana_
"""

# import webbrowser
# webbrowser.open("www.google.com")
import matplotlib.pyplot as plt

sentence = "lhrboeytobyiut breyt ov oiuhgdifgvb gnljfhdiuty[w gb iuyrtbhoyivbwepor"
letters = {}

for letter in sentence:
    letters[letter.lower()] = letters.get(letter,0) + 1

list_letters = list(letters.keys())
list_letters.sort()
for key in list_letters:
    print(f"{key} = {letters[key]}")
    
x,y = zip(*letters.items())
plt.bar(x,y)
plt.show()